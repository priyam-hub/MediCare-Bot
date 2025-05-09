document.addEventListener('DOMContentLoaded', () => {
    const chatButton = document.querySelector('.chat-button');
    const chatContainer = document.querySelector('.chat-container');
    const closeChat = document.querySelector('.close-chat');
    const sendMessage = document.querySelector('.send-message');
    const messageInput = document.querySelector('.chat-input input');
    const chatMessages = document.querySelector('.chat-messages');
  
    // Animate cards on scroll
    const animateOnScroll = () => {
      const cards = document.querySelectorAll('.service-card, .doctor-card');
      cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        const triggerBottom = window.innerHeight * 0.8;
  
        if (cardTop < triggerBottom) {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
        }
      });
    };
  
    document.querySelectorAll('.service-card, .doctor-card').forEach(card => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(50px)';
      card.style.transition = 'all 0.6s ease';
    });
  
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll();
  
    // Open chat window
    chatButton.addEventListener('click', () => {
      chatContainer.style.display = 'flex';
      setTimeout(() => {
        chatContainer.classList.add('active');
        chatButton.style.display = 'none';
      }, 10);
    });
  
    closeChat.addEventListener('click', () => {
      chatContainer.classList.remove('active');
      setTimeout(() => {
        chatContainer.style.display = 'none';
        chatButton.style.display = 'flex';
      }, 300);
    });
  
    const sendMessageHandler = () => {
      const message = messageInput.value.trim();
      if (message) {
        addMessage(message, 'user');
        messageInput.value = '';
  
        const typingIndicator = document.createElement('div');
        typingIndicator.classList.add('message', 'assistant-message', 'typing');
        typingIndicator.textContent = '...';
        chatMessages.appendChild(typingIndicator);
        chatMessages.scrollTop = chatMessages.scrollHeight;
  
        // Send message to Flask backend
        const formData = new FormData();
        formData.append('msg', message);
  
        fetch('/medical_chat', {
          method: 'POST',
          body: formData
        })
        .then(response => response.text())
        .then(reply => {
          typingIndicator.remove();
          addMessage(reply, 'assistant');
        })
        .catch(error => {
          typingIndicator.remove();
          addMessage('❌ Error: Could not connect to server.', 'assistant');
          console.error('Error:', error);
        });
      }
    };
  
    sendMessage.addEventListener('click', sendMessageHandler);
    messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        sendMessageHandler();
      }
    });
  
    function addMessage(text, sender) {
      const messageElement = document.createElement('div');
      messageElement.classList.add('message', `${sender}-message`);
      messageElement.textContent = text;
  
      messageElement.style.opacity = '0';
      messageElement.style.transform = 'translateY(20px)';
  
      chatMessages.appendChild(messageElement);
  
      setTimeout(() => {
        messageElement.style.opacity = '1';
        messageElement.style.transform = 'translateY(0)';
        messageElement.style.transition = 'all 0.3s ease';
      }, 10);
  
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        const headerOffset = 100;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
  
        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      });
    });
  });
  
# DEPENDENCIES

from pinecone import Pinecone
from pinecone import ServerlessSpec

from ..utils.logger import LoggerSetup

# LOGGER SETUP
index_manager_logger = LoggerSetup(logger_name = "index_manager.py", log_filename_prefix = "index_manager").get_logger()


class PineconeIndexManager:
    """
    A class to manage the creation of a Pinecone index for vector storage.
    """

    def __init__(self, api_key : str, index_name : str, dimension : int = 384,metric : str = "cosine", cloud : str = "aws", region : str = "us-east-1") -> None:
        
        """
        Initializes the Pinecone client and index configuration.

        Arguments:
            
            `api_key`                {str}          : Pinecone API key.
            
            `index_name`             {str}          : Name for the Pinecone index.
            
            `dimension`              {int}          : Dimension of the embedding vectors (default: 384).
            
            `metric`                 {str}          : Similarity metric to use (e.g., 'cosine').
            
            `cloud`                  {str}          : Cloud provider for hosting the index (default: 'aws').
            
            `region`                 {str}          : Cloud region for hosting the index (default: 'us-east-1').
        """
        
        self.api_key          = api_key
        self.index_name       = index_name
        self.dimension        = dimension
        self.metric           = metric
        self.cloud            = cloud
        self.region           = region
        self.pinecone_client  = Pinecone(api_key=self.api_key)

    def create_index(self):
        """
        Creates a new Pinecone index using the specified configuration.
        """
        self.pinecone_client.create_index(name       = self.index_name,
                                          dimension  = self.dimension,
                                          metric     = self.metric,
                                          spec       = ServerlessSpec(cloud   = self.cloud,
                                                                      region  = self.region
                                                                      )
                                        )

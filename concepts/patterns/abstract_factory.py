from abc import ABC, abstractmethod


# Abstract factories
class CloudProviderFactory(ABC):
    @abstractmethod
    def create_compute(self):
        pass

    @abstractmethod
    def create_storage(self):
        pass


# Concrete factories
class AWSFactory(CloudProviderFactory):
    def create_compute(self):
        return EC2Instance()

    def create_storage(self):
        return S3Bucket()


class AzureFactory(CloudProviderFactory):
    def create_compute(self):
        return AzureVM()

    def create_storage(self):
        return BlobStorage()


# Usage
def deploy_infrastructure(provider_factory: CloudProviderFactory):
    compute = provider_factory.create_compute()
    storage = provider_factory.create_storage()
    return compute, storage


aws_resources = deploy_infrastructure(AWSFactory())

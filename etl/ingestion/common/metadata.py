from datetime import datetime


def ingestion_metadata(source, dataset):

    return {

        "source": source,

        "dataset": dataset,

        "ingestion_time": datetime.utcnow().isoformat()
    }
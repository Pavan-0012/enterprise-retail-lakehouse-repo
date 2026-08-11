class SilverLogger:

    def log(
        self,
        dataset: dict,
        metrics: dict,
        execution_time: float
    ):

        print("\n" + "=" * 70)

        print("SILVER PIPELINE")

        print("=" * 70)

        print(f"Source              : {dataset['source']}")

        print(f"Bronze Table        : {dataset['bronze_table']}")

        print(f"Silver Table        : {dataset['silver_table']}")

        print(f"Rows Read           : {metrics['rows_before']}")

        print(f"Rows Written        : {metrics['rows_after']}")

        print(f"Duplicates Removed  : {metrics['duplicates_removed']}")

        print(f"Execution Time      : {execution_time:.2f} sec")

        print(f"Status              : {metrics['status']}")

        print("=" * 70)
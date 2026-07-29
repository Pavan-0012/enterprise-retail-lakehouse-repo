from etl.common.spark import SparkSessionFactory


def main():

    spark = SparkSessionFactory.create()

    print("=" * 60)
    print("Spark Version")
    print("=" * 60)

    print(spark.version)

    spark.stop()


if __name__ == "__main__":
    main()
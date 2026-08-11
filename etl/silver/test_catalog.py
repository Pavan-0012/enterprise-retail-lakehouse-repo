# from etl.common.spark import get_spark_session


# def main():

#     spark = get_spark_session()

#     print("\nSpark Version:")
#     print(spark.version)

#     print("\nCatalog Type:")
#     print(
#         spark.conf.get(
#             "spark.sql.catalog.enterprise.type"
#         )
#     )

#     print("\nWarehouse:")
#     print(
#         spark.conf.get(
#             "spark.sql.catalog.enterprise.warehouse"
#         )
#     )

#     print("\nNamespaces:")
#     spark.sql(
#         "SHOW NAMESPACES IN enterprise"
#     ).show(truncate=False)

#     spark.stop()


# if __name__ == "__main__":
#     main()


from etl.common.spark import get_spark_session

spark = get_spark_session()

print(
    spark.sparkContext._jsc.hadoopConfiguration().get(
        "fs.s3a.endpoint"
    )
)

df = spark.range(5)

df.write.mode("overwrite").parquet("s3a://silver/test")

print("SUCCESS")

spark.stop()
from seed.postgres.config import DATA_DIRECTORY, TABLE_MAPPING
from seed.postgres.database import get_engine
from seed.postgres.loader import PostgresLoader
from seed.postgres.validator import PostgresValidator


def main():

    engine = get_engine()

    loader = PostgresLoader(engine)
    validator = PostgresValidator(engine)

    print("=" * 75)
    print("POSTGRESQL SEEDING")
    print("=" * 75)

    for filename, table_name in TABLE_MAPPING.items():

        csv_path = DATA_DIRECTORY / filename

        if not csv_path.exists():
            print(f"⚠️  Skipping {filename} (File not found)")
            continue

        loader.load_table(csv_path, table_name)

    print("\n" + "=" * 75)
    print("VALIDATION")
    print("=" * 75)

    print(
        f"{'TABLE NAME':<20}"
        f"{'CSV COUNT':>15}"
        f"{'POSTGRES COUNT':>20}"
        f"{'STATUS':>10}"
    )

    print("-" * 75)

    success = True

    for filename, table_name in TABLE_MAPPING.items():

        csv_path = DATA_DIRECTORY / filename

        if not csv_path.exists():
            continue

        if not validator.validate(csv_path, table_name):
            success = False

    print("-" * 75)

    if success:
        print("✅ All tables validated successfully.")
    else:
        print("❌ Validation failed.")


if __name__ == "__main__":
    main()
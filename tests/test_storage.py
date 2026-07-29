from etl.storage.manager import StorageManager

manager = StorageManager(
    "enterprise-retail-lakehouse"
)

print(manager.exists())

for obj in manager.list_objects():

    print(obj.object_name)
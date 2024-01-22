from hash_table import HashTable


def main():
    hash_table = HashTable(5)
    hash_table.insert("apple", 10)
    hash_table.insert("orange", 20)
    hash_table.insert("banana", 30)
    hash_table.insert("pineapple", 40)
    hash_table.insert("mango", 50)
    hash_table.insert("grape", 60)

    print(f"apple: {hash_table.get('apple')}")
    print(f"table: {hash_table.table}")

    hash_table.remove("apple")

    print(f"apple: {hash_table.get('apple')}")
    print(f"table: {hash_table.table}")


if __name__ == "__main__":
    main()

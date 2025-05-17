def tampilkan_dictionary(data):
    print(f"{'key':<6}{'value':<8}{'item':<6}")
    for key, value in data.items():
        print(f"{str(key):<6}{str(value):<8}{str(key):<6}")


dict_sample = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
tampilkan_dictionary(dict_sample)

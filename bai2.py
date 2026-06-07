product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

for i, v in enumerate(product_list):
    raw = v.split("-")
    product_list[i] = {
        "id": raw[0],
        "name": raw[1],
        "price": raw[2],
        "rate": raw[3]
    }

def view_labels():
    print("--- DANH SÁCH TEM NHÃN ---")
    template = "Mã: {id:<10} | Tên: {name:<25} | Giá: {price} VND | Rating: {rate}*"

    for v in product_list:
        try:
            data = {
                "id": v["id"],
                "name": v["name"],
                "price": f"{int(v['price']):,}",
                "rate": v["rate"]
            }
            print(template.format_map(data))
        except:
            continue

def sort_products():
    def key_func(x):
        try:
            return (-float(x["rate"]), int(x["price"]))
        except:
            return (0, 10**18)

    product_list.sort(key=key_func)

    print("--- SẮP XẾP SẢN PHẨM ---")
    for i, v in enumerate(product_list):
        print(f"{i+1}. {v['id']}-{v['name']}-{v['price']}-{v['rate']}")

def total_value():
    total = 0
    for v in product_list:
        try:
            total += int(v["price"])
        except:
            continue

    print("--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND.")

while True:
    select = input("""
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng
4. Đóng hệ thống
================================================
Chọn chức năng (1-4): """)

    if select == "1":
        view_labels()
    elif select == "2":
        sort_products()
    elif select == "3":
        total_value()
    elif select == "4":
        print("Đóng hệ thống.")
        break
    else:
        print("Lựa chọn không hợp lệ!")
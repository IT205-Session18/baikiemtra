def menu():
    print("\nQUẢN LÝ KHO HÀNG - GROCERY STORE")
    print("\n1. Xem danh sách" +
          "\n2. Nhập thêm hàng hóa mới" +
          "\n3. Cập nhật số lượng tồn kho theo ID" +
          "\n4. Thoát chương trình")
def validate_input(prompt: str, input_type: str = "string"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Dữ liệu không được để trống, Nhập lại!")
            continue
        
        if input_type == "int":
            try:
                value = int(user_input)
                if value < 0:
                    print("Dữ liệu phải là số dương!")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ, Nhập lại!")
                continue
        return user_input
    
def show_inventory(inventory_list):
    if not inventory_list:
        print("Kho hàng hiện đang trống!")
        return
    print("Danh sách hàng tồn kho")
    print(f"{"ID":<8} | {"Tên hàng hóa":<20} | {"Số lượng tồn kho":<15}")
    for inventory in inventory_list:
        print(f"{inventory.get('id').upper():<8} | {inventory.get('name'):<20} | {inventory.get('quantity'):<15}")
def add_item(inventory_list):
    while True:
        id_inventory = validate_input("Nhập vào mã kho hàng: ","int")
        for inventory in inventory_list:
            if(id_inventory.lower() == inventory.get("id").lower()):
                print("Mã hàng này đã tồn tại, nhập lại ")
                break

        else:
            name_inventory = validate_input("Nhập vào tên kho hàng: ")
            quantity_inventory = validate_input("Nhập vào số lượng: ","int")
            new_inventory = {
                "id": id_inventory,
                "name": name_inventory,
                "quantity": quantity_inventory
            }
            inventory_list.append(new_inventory)
            print("Thêm hàng hóa vào kho thành công!")
            break

def update_quantity(inventory_list):
    if not inventory_list:
        print("Kho hàng đang trống!")
        return
    print("CẬP NHẬT SỐ LƯỢNG TỒN KHO")
    id_quantity = validate_input("Nhập mã hàng hóa cần sửa: ")
    for inventory in inventory_list:
        if (id_quantity.lower() == inventory.get("id").lower()):
            print(f"Tìm thấy hàng hóa: {inventory.get("name")} (Số lượng hiện tại: {inventory.get("quantity")})")
            quantity_store = validate_input("Nhập số lượng mới: ","int")
            inventory["quantity"] = quantity_store
            print("Cập nhật số lượng thành công!")
            break
    else:
        print(f"Không tìm thấy hàng hóa có mã {id_quantity}!")


def main():
    inventory_list = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
    ]

    while True:
        menu()
        choice = input("Vui lòng nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                show_inventory(inventory_list)
            case "2":
                add_item(inventory_list)
            case "3":
                update_quantity(inventory_list)
            case "4":
                print("Thoát chương trình !")
                break
            case _:
                print("Lỗi chỉ được nhập từ 1 tới 4")
main()
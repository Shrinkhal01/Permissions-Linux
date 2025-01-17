perm_values = {'r': 4, 'w': 2, 'x': 1}

def calculate_permission(permissions):
    user_perm = permissions[0:3]
    group_perm = permissions[3:6]
    others_perm = permissions[6:9]

    user_value = sum(perm_values[perm] for perm in user_perm if perm in perm_values)
    group_value = sum(perm_values[perm] for perm in group_perm if perm in perm_values)
    others_value = sum(perm_values[perm] for perm in others_perm if perm in perm_values)

    return f"{user_value}{group_value}{others_value}"

def main():
    print("File Permission Calculator (like `rwxr-xr--` format)")
    

    permissions = input("Enter permissions in `rwxrwxrwx` format (e.g., rwxr-xr--): ").strip()
    

    if len(permissions) != 9:
        print("Invalid input! Please enter exactly 9 characters (e.g., rwxr-xr--).")
        return
    

    numeric_permission = calculate_permission(permissions)
    

    print(f"Numeric Permission: {numeric_permission}")

if __name__ == "__main__":
    main()
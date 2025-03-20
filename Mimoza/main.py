import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    if os.name == 'nt':
        os.system('color 0A')  

def print_header():
    print("\033[92m")  
    print("_" * 30)
    print("                Проект Мимоза")
    print("-" * 35)
    print()
    print("            /\\_/\\           ┌───────────────┐")
    print("           ( o.o )          │ %пUHК о(12фfВ) │")
    print("           > ^ <  ──┐       │ >=1{(y >1 (1eP=KЖKfPч... │")
    print("          / | | |  │        └───────────────┘")
    print("         (  U U  ) │")
    print("                  └─────────────────────────")
    print("\033[0m")  

def print_menu():
    print("\033[96m")  
    print("1. Зашифровать файл")
    print("2. Расшифровать файл")
    print("3. Просмотреть доступные методы шифрования")
    print("4. Тестировать шифрование")
    print("5. Выход")
    print("\033[0m")  
    print()

# Метод шифрования Цезаря
def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    

    en_lower = "abcdefghijklmnopqrstuvwxyz"
    en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ru_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ru_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    for char in text:
        if char in en_lower:
            idx = en_lower.index(char)
            result += en_lower[(idx + shift) % len(en_lower)]
        elif char in en_upper:
            idx = en_upper.index(char)
            result += en_upper[(idx + shift) % len(en_upper)]
        elif char in ru_lower:
            idx = ru_lower.index(char)
            result += ru_lower[(idx + shift) % len(ru_lower)]
        elif char in ru_upper:
            idx = ru_upper.index(char)
            result += ru_upper[(idx + shift) % len(ru_upper)]
        else:
            result += char
    
    return result

# Метод шифрования замены (простая подстановка)
def substitution_cipher(text, key, decrypt=False):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
    substitution = key + ''.join([c for c in alphabet if c not in key])
    
    result = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in alphabet:
            idx = alphabet.find(lower_char)
            if decrypt:
               
                sub_char = alphabet[substitution.find(lower_char)]
            else:

                sub_char = substitution[idx]
                

            if char.isupper():
                result += sub_char.upper()
            else:
                result += sub_char
        else:
            result += char
    
    return result

# Метод шифрования Виженера
def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key = key.lower()
    key_idx = 0
    

    en_lower = "abcdefghijklmnopqrstuvwxyz"
    en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ru_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ru_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    for char in text:

        if char in en_lower:

            key_char = key[key_idx % len(key)]

            if key_char in ru_lower:
                key_shift = ru_lower.index(key_char) % len(en_lower)
            else:
                key_shift = en_lower.index(key_char) if key_char in en_lower else 0
                
            if decrypt:
                key_shift = -key_shift
                
            idx = en_lower.index(char)
            result += en_lower[(idx + key_shift) % len(en_lower)]
            key_idx += 1
            
        elif char in en_upper:
            key_char = key[key_idx % len(key)]
            if key_char in ru_lower:
                key_shift = ru_lower.index(key_char) % len(en_lower)
            else:
                key_shift = en_lower.index(key_char) if key_char in en_lower else 0
                
            if decrypt:
                key_shift = -key_shift
                
            idx = en_upper.index(char)
            result += en_upper[(idx + key_shift) % len(en_upper)]
            key_idx += 1
            

        elif char in ru_lower:
            key_char = key[key_idx % len(key)]
            if key_char in en_lower:
                key_shift = en_lower.index(key_char) % len(ru_lower)
            else:
                key_shift = ru_lower.index(key_char) if key_char in ru_lower else 0
                
            if decrypt:
                key_shift = -key_shift
                
            idx = ru_lower.index(char)
            result += ru_lower[(idx + key_shift) % len(ru_lower)]
            key_idx += 1
            
        elif char in ru_upper:
            key_char = key[key_idx % len(key)]
            if key_char in en_lower:
                key_shift = en_lower.index(key_char) % len(ru_lower)
            else:
                key_shift = ru_lower.index(key_char) if key_char in ru_lower else 0
                
            if decrypt:
                key_shift = -key_shift
                
            idx = ru_upper.index(char)
            result += ru_upper[(idx + key_shift) % len(ru_upper)]
            key_idx += 1
            
        else:
            result += char
    
    return result

# Метод транспозиции (перестановки)
def transposition_cipher(text, key, decrypt=False):
    result = ""
    

    if not decrypt:
        text = text.replace(" ", "")
    

    num_columns = len(key)
    

    num_rows = (len(text) + num_columns - 1) // num_columns
    

    if not decrypt:

        matrix = [[''] * num_columns for _ in range(num_rows)]
        

        idx = 0
        for row in range(num_rows):
            for col in range(num_columns):
                if idx < len(text):
                    matrix[row][col] = text[idx]
                    idx += 1
                else:

                    matrix[row][col] = ' '
        

        key_order = sorted(range(num_columns), key=lambda i: key[i])
        

        for col_idx in key_order:
            for row in range(num_rows):
                result += matrix[row][col_idx]
    else:

        matrix = [[''] * num_columns for _ in range(num_rows)]
        

        key_order = sorted(range(num_columns), key=lambda i: key[i])
        

        idx = 0
        for col_idx in key_order:
            for row in range(num_rows):
                if idx < len(text):
                    matrix[row][col_idx] = text[idx]
                    idx += 1
        

        for row in range(num_rows):
            for col in range(num_columns):
                result += matrix[row][col]
        

        result = result.rstrip()
    
    return result

# Метод собственного шифрования с уникальным ключом
def custom_cipher(text, key, decrypt=False):
    result = ""
    key_str = str(key)
    key_sum = sum(ord(c) for c in key_str)
    unique_seed = key_sum % 100 + 1  
    

    en_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ru_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    digits = "0123456789"
    special = ",.!?;:-_+=*&^%$#@()[]{}|\\/<>\"'"

    chinese = "的一是不了人我在有他这为之大来以个中上们到说国和地也子时道出而要于就下得可你年生"
    chinese += "自会那后能对着事其里所去行过家十用发天如然作方成者多日都三小军二公无上么经法"
    chinese += "当起定做被行动所说常与现其进此点外科门近事界位示真务今主动表正开部必然已用形"
    
    all_chars = en_letters + ru_letters + digits + special + chinese
    

    char_map = list(all_chars)
    

    mixed_chars = list(all_chars)
    for i in range(len(mixed_chars) - 1, 0, -1):

        j = (ord(mixed_chars[i]) * i * unique_seed) % len(mixed_chars)
        mixed_chars[i], mixed_chars[j] = mixed_chars[j], mixed_chars[i]
    
    for char in text:
        if char in all_chars:
            idx = all_chars.find(char)
            if decrypt:

                try:
                    idx_in_mixed = mixed_chars.index(char)
                    result += all_chars[idx_in_mixed]
                except ValueError:

                    result += char
            else:

                result += mixed_chars[idx]
        else:

            result += char
            
    return result


encryption_methods = {
    "1": {"name": "Шифр Цезаря", "function": caesar_cipher, "param": "сдвиг (число)"},
    "2": {"name": "Шифр замены", "function": substitution_cipher, "param": "ключ (строка букв)"},
    "3": {"name": "Шифр Виженера", "function": vigenere_cipher, "param": "ключевое слово"},
    "4": {"name": "Транспозиция", "function": transposition_cipher, "param": "ключевое слово"},
    "5": {"name": "Уникальный шифр", "function": custom_cipher, "param": "секретный ключ"}
}

def encrypt_file():
    clear_screen()
    print_header()
    print("\033[93m")  
    print("ШИФРОВАНИЕ ФАЙЛА")
    print("-" * 30)
    print("\033[0m")  
    

    print("\033[96m")  
    print("Доступные методы шифрования:")
    for method_id, details in encryption_methods.items():
        print(f"{method_id}. {details['name']} ({details['param']})")
    print("\033[0m")  
    print()
    

    file_path = input("\033[97mВведите путь к файлу для шифрования: \033[0m").strip()
    if not os.path.exists(file_path):
        print(f"\033[91mОшибка: Файл '{file_path}' не существует.\033[0m")
        input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
        return
    
    method_id = input("\033[97mВыберите метод шифрования (1-5): \033[0m").strip()
    if method_id not in encryption_methods:
        print("\033[91mОшибка: Неверный метод шифрования.\033[0m")
        input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
        return
    
    method = encryption_methods[method_id]
    key = input(f"\033[97mВведите {method['param']}: \033[0m").strip()
    

    if method_id == "1":  # Шифр Цезаря
        try:
            key = int(key)
            if key < 1 or key > 25:
                print("Ошибка: Сдвиг должен быть числом от 1 до 25.")
                input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
                return
        except ValueError:
            print("Ошибка: Сдвиг должен быть числом.")
            input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
            return
    

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
        return
    

    try:
        encrypted_content = method["function"](content, key)
    except Exception as e:
        print(f"Ошибка при шифровании: {e}")
        input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
        return
    

    file_name, file_ext = os.path.splitext(os.path.basename(file_path))
    

    encrypted_file_path = os.path.join(os.path.dirname(file_path), f"{file_name} {method_id}{file_ext}")
    

    try:
        with open(encrypted_file_path, 'w', encoding='utf-8') as file:
            file.write(encrypted_content)
        print(f"\033[92mФайл успешно зашифрован и сохранен как '{encrypted_file_path}'\033[0m")
    except Exception as e:
        print(f"Ошибка при записи зашифрованного файла: {e}")
    
    input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")

def decrypt_file():
    clear_screen()
    print_header()
    print("\033[93m")  
    print("РАСШИФРОВКА ФАЙЛА")
    print("-" * 30)
    print("\033[0m")  
    

    file_path = input("\033[97mВведите путь к зашифрованному файлу: \033[0m").strip()
    if not os.path.exists(file_path):
        print(f"\033[91mОшибка: Файл '{file_path}' не существует.\033[0m")
        input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
        return
    

    file_name = os.path.basename(file_path)
    method_id = None
    

    # 1
    parts = file_name.split()
    if parts and parts[-1][-1] in encryption_methods:
        method_id = parts[-1][-1]
    
    # 2
    if method_id is None:
        file_name_without_ext, file_ext = os.path.splitext(file_name)
        if file_name_without_ext and file_name_without_ext[-1] in encryption_methods:
            method_id = file_name_without_ext[-1]
    
    # 3
    if method_id is None and ' ' in file_name:
        last_part = file_name.split()[-1]
        for char in last_part:
            if char in encryption_methods:
                method_id = char
                break
    
    if method_id is None or method_id not in encryption_methods:

        print("Предупреждение: Не удалось автоматически определить метод шифрования из имени файла.")
        print("Доступные методы шифрования:")
        for m_id, details in encryption_methods.items():
            print(f"{m_id}. {details['name']}")
        
        method_id = input("\nВведите номер метода шифрования (1-5): ").strip()
        if method_id not in encryption_methods:
            print("Ошибка: Неверный метод шифрования.")
            input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
            return
    
    method = encryption_methods[method_id]
    print(f"Используемый метод шифрования: {method['name']}")
    
    key = input(f"\033[97mВведите {method['param']} для расшифровки: \033[0m").strip()
    

    if method_id == "1":  # Шифр Цезаря
        try:
            key = int(key)
            if key < 1 or key > 25:
                print("Ошибка: Сдвиг должен быть числом от 1 до 25.")
                input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
                return
        except ValueError:
            print("Ошибка: Сдвиг должен быть числом.")
            input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
            return
    

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
        return
    

    try:
        decrypted_content = method["function"](content, key, decrypt=True)
    except Exception as e:
        print(f"Ошибка при расшифровке: {e}")
        input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")
        return
    

    file_name_with_ext = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(file_name_with_ext)
    

    parts = file_name.split()
    if parts and parts[-1][-1] in encryption_methods:
        parts[-1] = parts[-1][:-1]
        if not parts[-1]:  
            parts.pop()
    decrypted_file_path = os.path.join(os.path.dirname(file_path), ' '.join(parts) + "_decrypted" + file_ext)
    

    try:
        with open(decrypted_file_path, 'w', encoding='utf-8') as file:
            file.write(decrypted_content)
        print(f"\033[92mФайл успешно расшифрован и сохранен как '{decrypted_file_path}'\033[0m")
    except Exception as e:
        print(f"Ошибка при записи расшифрованного файла: {e}")
    
    input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")

def show_encryption_methods():
    clear_screen()
    print_header()
    print("\033[93m")  
    print("ДОСТУПНЫЕ МЕТОДЫ ШИФРОВАНИЯ")
    print("-" * 30)
    print("\033[0m")  
    
    for method_id, details in encryption_methods.items():
        print(f"\033[96m{method_id}. {details['name']}\033[0m")
        print(f"\033[97m   Параметр: {details['param']}\033[0m")
        print()
    
    input("\033[97mНажмите Enter для возврата в главное меню...\033[0m")

def main():
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input("\033[97mВыберите действие (1-5): \033[0m").strip()
        
        if choice == "1":
            encrypt_file()
        elif choice == "2":
            decrypt_file()
        elif choice == "3":
            show_encryption_methods()
        elif choice == "4":
            test_functionality()
        elif choice == "5":
            clear_screen()
            print("Спасибо за использование программы!")
            time.sleep(1.5)
            sys.exit(0)
        else:
            print("Ошибка: Неверный выбор. Пожалуйста, выберите 1-5.")
            time.sleep(1.5)

def test_functionality():

    test_content = "Это тестовый текст для проверки работы программы шифрования и расшифрования.\nАБВГД абвгд ABCDE abcde 12345"
    test_file = "test_encryption.txt"
    
    try:
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        print(f"Создан тестовый файл: {test_file}")
        print("Оригинальное содержимое:")
        print("-" * 40)
        print(test_content)
        print("-" * 40)
        

        for method_id, method_info in encryption_methods.items():
            print(f"\nТестирование метода: {method_info['name']}")
            

            test_key = "3" if method_id == "1" else "ключ"
            if method_id == "1":
                test_key = int(test_key)
            

            encrypted_content = method_info["function"](test_content, test_key)
            encrypted_file = f"test_encrypted {method_id}.txt"
            
            with open(encrypted_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_content)
            
            print(f"Создан зашифрованный файл: {encrypted_file}")
            print("Зашифрованное содержимое:")
            print("-" * 40)
            print(encrypted_content[:100] + "..." if len(encrypted_content) > 100 else encrypted_content)
            print("-" * 40)
            

            decrypted_content = method_info["function"](encrypted_content, test_key, decrypt=True)
            decrypted_file = f"test_decrypted {method_id}.txt"
            
            with open(decrypted_file, 'w', encoding='utf-8') as f:
                f.write(decrypted_content)
            
            print(f"Создан расшифрованный файл: {decrypted_file}")
            print("Расшифрованное содержимое:")
            print("-" * 40)
            print(decrypted_content)
            print("-" * 40)
            

            if decrypted_content == test_content:
                print("✓ Тест успешно пройден - содержимое совпадает с оригиналом")
            else:
                print("✗ Тест НЕ пройден - содержимое отличается от оригинала")
                print("Различия:")
                for i, (orig_char, decr_char) in enumerate(zip(test_content, decrypted_content)):
                    if orig_char != decr_char:
                        print(f"Позиция {i}: '{orig_char}' -> '{decr_char}'")
                        if i > 10:
                            break
            
            input("\nНажмите Enter для продолжения тестирования...")
            clear_screen()
        
        print("Тестирование завершено.")
        input("\033[97mНажмите Enter для запуска основной программы...\033[0m")
        
    except Exception as e:
        print(f"Ошибка при тестировании: {e}")
        input("\033[97mНажмите Enter для запуска основной программы...\033[0m")

if __name__ == "__main__":
    try:
        # test_functionality()  
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\nПрограмма завершена.")
        sys.exit(0) 
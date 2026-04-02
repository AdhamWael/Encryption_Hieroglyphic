import string

def encrypt_name():
    # STEP 1
    print("=== HIEROGLYPHIC NAME ENCRYPTION SYSTEM ===")
    input("Press Enter to begin...")
    
    # STEP 2
    parent_name = input("\nEnter parent name: ")
    
    # STEP 3
    print(f"\nWelcome, {parent_name}.")
    print("This system will encrypt your name using the function f(x) = 3x + 2 mod 26.")
    print("Then it will show the encrypted letters and their hieroglyphic symbols.")
    
    # Process Name (Remove spaces and symbols)
    letters_only = "".join([c for c in parent_name if c.lower() in string.ascii_lowercase]).upper()
    
    # STEP 4
    print("\n=== ORIGINAL LETTERS ===")
    print(f"Name entered: {parent_name}")
    print(f"Letters used: {letters_only}")
    
    if not letters_only:
        print("\nNo valid letters found in the name. Exiting...")
        return
        
    # Dictionary for alphabet-to-number (A=1 ... Z=26)
    alpha_to_num = {chr(65+i): i+1 for i in range(26)}
    
    # Reverse dictionary for number-to-letter
    num_to_alpha = {i+1: chr(65+i) for i in range(26)}
    
    # STEP 5
    original_numbers = []
    for char in letters_only:
        num = alpha_to_num[char]
        original_numbers.append(num)
        
    orig_nums_str = ", ".join(map(str, original_numbers))
    print("\n=== ORIGINAL NUMBERS ===")
    print("A = 1, B = 2, ... Z = 26")
    print(f"Original numbers: {orig_nums_str}")
    
    # STEP 6
    print("\n=== ENCRYPTION RULE ===")
    print("For each letter number x, compute:")
    print("f(x) = 3x + 2 mod 26")
    print("If the result is 0, use 26.")
    
    # Process Encryption
    encrypted_numbers = []
    encrypted_letters = []
    # Using Unicode Egyptian Hieroglyphs (from U+13000)
    # Hieroglyphic map from user provided table
    hieroglyph_map = {
        'A': '𓄿', 'B': '𓃀', 'C': '𓍿', 'D': '𓂧', 'E': '𓇋',
        'F': '𓆑', 'G': '𓎼', 'H': '𓉔', 'I': '𓇋', 'J': '𓆓',
        'K': '𓎡', 'L': '𓃭', 'M': '𓅓', 'N': '𓈖', 'O': '𓂝',
        'P': '𓊪', 'Q': '𓈎', 'R': '𓂋', 'S': '𓋴', 'T': '𓏏',
        'U': '𓅱', 'V': '𓆑', 'W': '𓅱', 'X': '𓐍', 'Y': '𓇋',
        'Z': '𓊃'
    }
    
    for x in original_numbers:
        # Encryption function f(x) = 3x + 2 mod 26
        result = (3 * x + 2) % 26
        
        # Add the project rule: if the mod result is 0, convert it to 26.
        if result == 0:
            result = 26
            
        encrypted_numbers.append(result)
        
        # Convert numbers back to letters using the reverse table
        encrypted_letter = num_to_alpha[result]
        encrypted_letters.append(encrypted_letter)
        
    enc_nums_str = ", ".join(map(str, encrypted_numbers))
    enc_letters_str = ", ".join(encrypted_letters)
    enc_letters_joined = "".join(encrypted_letters)
    
    # STEP 7
    print("\n=== ENCRYPTED NUMBERS ===")
    print(f"Encrypted numbers: {enc_nums_str}")
    
    # STEP 8
    print("\n=== ENCRYPTED LETTERS ===")
    print(f"Encrypted letters: {enc_letters_str}")
    
    # STEP 9
    print("\n=== HIEROGLYPHIC SYMBOLS ===")
    hieroglyph_version = ""
    for letter in encrypted_letters:
        symbol = hieroglyph_map[letter]
        hieroglyph_version += symbol
        print(f"{letter} -> {symbol}")
        
    print(f"Final hieroglyphic name: {hieroglyph_version}")
    
    # STEP 10
    print("\n=== FINAL SUMMARY ===")
    print(f"Parent name: {parent_name}")
    print(f"Original letters: {letters_only}")
    print(f"Original numbers: {orig_nums_str}")
    print(f"Encrypted numbers: {enc_nums_str}")
    print(f"Encrypted letters: {enc_letters_joined}")
    print(f"Hieroglyphic version: {hieroglyph_version}")
    print("Encryption complete.")

# Test section for short and long names
def run_tests():
    print("\n--- AUTOMATED TESTING ---")
    test_names = ["A", "Ali", "Christopher"]
    for name in test_names:
        print(f"\nTesting name: {name}")
        letters_only = "".join([c for c in name if c.lower() in string.ascii_lowercase]).upper()
        # Encryption check
        for char in letters_only:
            x = ord(char) - 64
            enc = (3 * x + 2) % 26
            if enc == 0: enc = 26
            print(f"{char}({x}) -> {enc}({chr(enc+64)})")
    print("--- TESTS COMPLETE ---\n")

if __name__ == "__main__":
    import sys
    # Quick simple way to run tests if '--test' is passed
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        run_tests()
    else:
        encrypt_name()

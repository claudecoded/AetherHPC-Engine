import os
import base64
import hashlib

def decrypt_payload(encrypted_string, secret_salt="AetherHPCSupremeKey"):
    key = hashlib.sha256(secret_salt.encode()).hexdigest()
    decoded_data = base64.urlsafe_b64decode(encrypted_string.encode()).decode()
    decoded_chars = []
    for i in range(len(decoded_data)):
        key_c = key[i % len(key)]
        decoded_c = chr(ord(decoded_data[i]) ^ ord(key_c))
        decoded_chars.append(decoded_c)
    return "".join(decoded_chars)

if __name__ == "__main__":
    print("[MASTER CONSOLIDATOR] Gathering computing blocks from decentralized vault storage...")
    input_dir = "all-shards"
    output_file = "mainframe_output/super_compute_final_report.dat"
    os.makedirs("mainframe_output", exist_ok=True)

    with open(output_file, "w") as master_f:
        master_f.write("=== AETHERHPC MAINOS PRODUCTION DATA PAYLOAD ===\n\n")
        
        if os.path.exists(input_dir):
            for root, dirs, files in os.walk(input_dir):
                for file in files:
                    if file.endswith(".enc"):
                        file_path = os.path.join(root, file)
                        with open(file_path, "r") as f:
                            encrypted_content = f.read()
                        try:
                            decrypted_content = decrypt_payload(encrypted_content)
                            master_f.write(decrypted_content + "\n" + "="*50 + "\n")
                            print(f"[CONSOLIDATION SUCCESS] Integrated block: {file}")
                        except Exception as e:
                            print(f"[CORRUPTION ERROR] Failed reading shard {file}: {e}")
                            
    print(f"[MASTER CONSOLIDATOR] Super-Dataset generation complete: {output_file}")

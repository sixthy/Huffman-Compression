## Virtual Environment

- The `.venv` folder is generated locally and is not versioned in Git.
- Each developer creates their own virtual environment when cloning the repository.
- Files in `Compressed_Files/` and `Decompress_Files/` are temporary and not versioned.

### Prerequisites
- Python 3.10 or higher

## Steps to Run

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd projeto
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Run the Program
```bash
python main.py
```

## How to Use

Edit the `main.py` file and modify these variables:
- `base = "Input/Text1.txt"` (input file)
- `out = "Compressed_Files/Text1_encoded.txt"` (compressed output)
- `outD = "Decompress_Files/Text1_decoded.txt"` (decompressed output)

The program will:
1. Read the input file
2. Compress using Huffman algorithm
3. Decompress the file
4. Save the results in the specified folders

## Troubleshooting

### "Python not found"
- Install Python 3.10+ or activate the virtual environment manually

### Output files not appearing
- Confirm that `Compressed_Files/` and `Decompress_Files/` folders exist
- Run the program again

## Test Files

The project includes test files: Text1.txt through Text6.txt in the `Input/` folder
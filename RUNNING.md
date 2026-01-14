## 1. Start the Backend (FastAPI)
This handles the database and API logic.

> **Note**: These commands are for **Windows PowerShell** or **Command Prompt**.
> If you are using WSL (Linux), you cannot use the Windows `venv`.

1. Open a new terminal.
2. Navigate to the backend directory:n
   ```powershell
   cd "Book-keeping Backend"
   ```
3. Install dependencies (if not already installed):
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the server
   ```powershell
   uvicorn app.main:app --reload
   ```

## 2. Start the Frontend (React + Vite)
This runs the user interface.

1. Open a **second** terminal.
2. Navigate to the frontend directory:
   ```powershell
   cd "Book-keeping Application"
   ```
3. Run the development server:
   ```powershell
   npm run dev
   ```

## Tips
- **Docs**: Backend API docs are at `http://localhost:8000/docs`.
- **Login**: Use the admin credentials (`admin@matura.co` / `admin123`) to log in.

## Troubleshooting

### "Cannot find module @rollup/rollup-linux..."
This happens if you install dependencies on Windows (PowerShell) but try to run on Linux (WSL), or vice versa.
**Fix**:
1. Delete `node_modules` and `package-lock.json`.
2. Run `npm install` again **inside the terminal you intend to use** (e.g., if using WSL, run `npm install` in WSL).

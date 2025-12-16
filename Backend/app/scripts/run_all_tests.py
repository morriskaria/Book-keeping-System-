import subprocess
import sys
import os

SCRIPTS = [
    "app/scripts/test_billing.py",
    "app/scripts/test_payments.py",
    "app/scripts/test_expenses.py",
    "app/scripts/test_payroll.py",
    "app/scripts/test_inventory.py",
    "app/scripts/test_reports.py",
    "app/scripts/test_validation.py"
]

def run_tests():
    print("="*60)
    print("RUNNING ALL SYSTEM TESTS - HOSPITAL BOOKKEEPING")
    print("="*60)
    
    env = os.environ.copy()
    # Ensure PYTHONPATH includes current directory
    env["PYTHONPATH"] = os.getcwd()
    
    failures = []
    
    for script in SCRIPTS:
        print(f"\n>> Running {script}...")
        try:
            # Run the script using the current python interpreter
            result = subprocess.run(
                [sys.executable, script], 
                env=env, 
                capture_output=True, 
                text=True
            )
            
            if result.returncode == 0:
                print(f"[PASS]: {script}")
                # Optional: Print output if needed (or just verify it ran)
                # print(result.stdout)
            else:
                print(f"[FAIL]: {script}")
                print("--- Error Output ---")
                print(result.stderr)
                # print(result.stdout)
                failures.append(script)
                
        except Exception as e:
            print(f"[ERROR]: Could not run {script}: {e}")
            failures.append(script)

    print("\n" + "="*60)
    if failures:
        print(f"SUMMARY: {len(failures)} Tests FAILED.")
        for f in failures:
            print(f" - {f}")
        sys.exit(1)
    else:
        print("SUMMARY: ALL TESTS PASSED! SYSTEM IS HEALTHY.")
        sys.exit(0)

if __name__ == "__main__":
    run_tests()

# --- NumScript ---

if __name__ == "__main__":  
    
    # --- Importing NumScript Virtual Machine from Source ---
    from Source.builder import NumScriptVirtualMachine

    # --- Launching the NumScript shell ---                
    shell = NumScriptVirtualMachine()
    shell.cli()
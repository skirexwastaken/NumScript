# --- NumScript ---

# --- Importing NumScript Virtual Machine from Source ---
from Source.builder import NumScriptVirtualMachine

# --- Launching the NumScript shell ---                
engine = NumScriptVirtualMachine()
engine.cli()
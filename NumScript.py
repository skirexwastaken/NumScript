# --- NumScript ---

# --- Importing NumScript Virtual Machine from source ---
from source.builder import NumScriptVirtualMachine

# --- Launching the NumScript shell ---                
engine = NumScriptVirtualMachine()

# --- Removing KeyboardInterrupt error message ---
try:
    engine.cli()

except KeyboardInterrupt:
    pass
from __main__ import pth

## Defines path and file names to each component.
## Done using os.path to be file system independant.
HOME = pth.abspath('./OHRbIT_SIMULATOR')
CORE = pth.abspath('./OHRbIT_SIMULATOR/core_tools')

ACC = pth.abspath('./OHRbIT_SIMULATOR/read_accelerations')
COMS = pth.abspath('./OHRbIT_SIMULATOR/read_accelerations/comsol')
PRE = pth.abspath('./OHRbIT_SIMULATOR/read_accelerations/preprocessed')
PNP = pth.abspath('./OHRbIT_SIMULATOR/read_accelerations/processed_np')
#acc_file = pth.abspath('./OHRbIT_SIMULATOR/read_accelerations/preprocessed/df_text.txt')
acc_file = pth.abspath('./OHRbIT_SIMULATOR/read_accelerations/preprocessed/Test')

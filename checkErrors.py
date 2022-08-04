import glob
import sys

ignoredErrors = [
    "Error in <TTree::SetBranchAddress>: unknown branch",
    "Error in <TSystem::ExpandFileName>: input: $HOME/.root.mimes, output: $HOME/.root.mimes",
    ".root"
]

if __name__ == "__main__":
    # open all files with tag and loop
    jobName = sys.argv[1]
    jobID = sys.argv[2] if (len(sys.argv) >= 3) else "*"
    files = glob.glob("/user/nivanden/condor/error/jobName*"+jobID+"*")
    problematic = []

    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if any(error in line for error in ignoredErrors): continue
                problematic.append(file)

    
    for file in problematic:
        rootfilename = ""
        skip = False
        basketBufferErr = False
        with open(file, 'r') as f:
            for i, line in enumerate(f):
                if skip:
                    skip = False
                    continue
                if i == 0: continue
                if i == 1: 
                    rootfilename = line.rstrip()
                    continue
                if "Error in <TBasket::ReadBasketBuffers>:" in line:
                    if not basketBufferErr: print("sample {} has bad write -> reproduce sample!".format(rootfilename))
                    skip = True
                    basketBufferErr = True
                else:
                    print("unknown error: {}".format(line))
                    print("in file "+file)

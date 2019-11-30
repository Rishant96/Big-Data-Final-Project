import glob
import pandas as pd

def get_output(predictions, output_file, input_folder_name='testing_portfolios'):
    path = input_folder_name # use your path
    all_files = glob.glob(path + "/*.csv")
    print(f'found {len(all_files)} files.')
    files = []
    for f in all_files:
        t = f[24:]
        t = t[:-4]
        files.append(t)
    def sort_file(item):
        return int(item.split('_')[1])
    files = sorted(files, key=sort_file)
    assert len(predictions) == len(files)
    output = []
    print(f'constructing output for {len(predictions)} predictions')
    for i in range(len(predictions)):
        pred = predictions[i]
        output.append((files[i], pred))

    if output_file is not None:
        op_pd = pd.DataFrame(output, columns=['ID','ln_LR'])
        op_pd.to_csv(output_file + '.csv', index=False)
        return op_pd
    else:
        return output
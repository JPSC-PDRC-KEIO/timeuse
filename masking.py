import random
import pathlib
import numpy as np

"""[summary]
テスト用データの作成
"""
base_dir = pathlib.Path("/mnt/d/jpsc_data/fixed_width/p29_release/p29")
data_file = pathlib.Path("p29_3.txt")
taraget_file = base_dir / data_file

print(taraget_file)

last_id = 5650  # 　一番若いID
with open(taraget_file, "r") as f1, open("dummy.txt", "w") as f2:
    data_array = np.genfromtxt(f1.readlines(), delimiter=1, dtype="str")
    num_lines = data_array.shape[0]
    k = 5  # 抽出数
    smpl_rows = random.sample(range(num_lines), k)  # 抽出行
    smpl = data_array[smpl_rows]
    print(smpl)
    masking_id = [str(i).zfill(4) for i in random.sample(range(last_id), k)]
    masking_id_array = np.array(
        [[m for m in str(mid)] for mid in masking_id])
    print(masking_id_array)
    smpl[:, 0:4] = masking_id_array
    smpl1 = smpl.astype(str)
    smpl1[:, 12:173] = " "
    smpl1[:, 337:] = " "
    print(smpl1)
    np.savetxt(f2, smpl1, delimiter="", fmt="%s")

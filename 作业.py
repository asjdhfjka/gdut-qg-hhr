import numpy as np
import json
class system:
    def __init__(self,vectors,ori_axis):
        self.vectors =np.array(vectors, dtype=np.float64)
        self.ori_axis=np.array(ori_axis, dtype=np.float64)
        self.dim = self.ori_axis.shape[1]
    def _valid(self,axis):
        axis_np = np.array(axis, dtype=np.float64)
        if axis_np.shape[0]!= axis_np.shape[1]:
            return False
        if np.linalg.matrix_rank(axis_np) != axis_np.shape[0]:#矩阵的秩，表示矩阵中线性无关的行（或列）的最大数目
            return False
        return True
    def change_axis(self,obj_axis):
        valid=self._valid(obj_axis)
        if not valid:
            print("目标坐标徐不合法")
            return
        obj_axis_np=np.array(obj_axis, dtype=np.float64)
        transform_mat = np.linalg.inv(obj_axis_np) @ self.ori_axis
        self.cur_vectors = self.vectors @ transform_mat.T
        self.cur_axis= obj_axis_np
        return self.cur_vectors
    def axis_projection(self):
        projections = []
        axis_length= np.linalg.norm(self.cur_axis, axis=1)
        for vec in self.cur_vectors:
            vec_proj = []
            for i, axis in enumerate(self.cur_axis):
                proj= np.dot(vec, axis) / axis_length[i]
                vec_proj.append(proj)
            projections.append(vec_proj)
        return projections
    def axis_angle(self):
        angles = []
        axis_norms = np.linalg.norm(self.cur_axis, axis=1)
        for vec in self.cur_vectors:
            vec_norm = np.linalg.norm(vec)
            if vec_norm == 0:
                angles.append([0.0] * self.dim)#零向量特殊处理
                continue
            vec_angles = []
            for i, axis in enumerate(self.cur_axis):
                dot = np.dot(vec, axis)
                cos= dot / (vec_norm * axis_norms[i])
                cos= np.clip(cos, -1.0, 1.0)
                finalangle = np.arccos(cos)
                vec_angles.append(finalangle)
            angles.append(vec_angles)
        return angles
    def area_scale(self):
        det = np.linalg.det(self.cur_axis)
        return abs(det)
    def read_tasks(self, tasks):
        results = {}
        for idx, task in enumerate(tasks):
            task_type = task["type"]
            task_key = f"task_{idx}_{task_type}"
            if task_type == "change_axis":
                new_vecs = self.change_axis(task["obj_axis"])
                results[task_key] = {
                    "new_vectors": new_vecs.tolist(),
                    "new_axis": task["obj_axis"]
                }
            elif task_type == "axis_projection":
                results[task_key] = {
                    "projections": self.axis_projection()
                }
            elif task_type == "axis_angle":
                results[task_key] = {
                    "angles": self.axis_angle()
                }
            elif task_type == "area":
                results[task_key] = {
                    "area_scale": self.area_scale()
                }
            else:
                results[task_key] = {"status": "failed", "error": f"未知任务类型：{task_type}"}
        return results
def main(json_path):
        with open('qg', "r", encoding="utf-8") as f:
            data = json.load(f)
        cs = system(data["ori_axis"], data["vectors"])
        results = cs.read_tasks(data["tasks"])
        print(f"任务组名称：{data['group_name']}")
        print("=" * 60)
        for task_key, res in results.items():
            print(f"任务：{task_key}")
            for k, v in res.items():
                if k != "status":
                    print(f"{k}：{v}")
if __name__ == "__main__":
    main("qg.json")
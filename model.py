import pandas as pd
from surprise import Dataset, Reader, SVD

def recommend(data, target_user_id, top_n = 100):
    """
    data: List[UserCourseScore]
    return: List of {courseId, predicted_score}
    """
    # 转为 DataFrame
    df = pd.DataFrame([{
        "user": d.userId,
        "item": d.courseId,
        "rating": d.score
    } for d in data])

    # Surprise 需要的 Reader
    reader = Reader(rating_scale=(0, 10))
    dataset = Dataset.load_from_df(df[["user", "item", "rating"]], reader)

    trainset = dataset.build_full_trainset()

    # 使用 SVD 算法
    algo = SVD()
    algo.fit(trainset)

    # 所有的课程
    all_items = df["item"].unique()

    # 已学课程
    learned_items = set(df[df["user"] == target_user_id]["item"])

    # 预测未学课程
    predictions = []
    for item in all_items:
        if item not in learned_items:
            pred = algo.predict(target_user_id, item)
            predictions.append({
                "courseId": int(item),
                "score": float(pred.est)
            })

    # 按预测评分排序
    predictions.sort(key=lambda x: x["score"], reverse=True)
    # 返回候选池
    return predictions[:top_n]
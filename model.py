from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np

#以下の処理を関数化
def predict(input_filename):
    #認識させたい画像の読み込み
    input_image = image.load_img(input_filename, target_size=(224,224))

    #画像の前処理
    input = image.img_to_array(input_image)

    input = np.expand_dims(input,axis=0)

    input = preprocess_input(input)

    #既存モデルの導入
    model = VGG16(weights='imagenet')

    #画像を予測
    results = model.predict(input)

    #予測結果とクラス名を紐付け（上位５クラスまで）
    decode_results = decode_predictions(results, top=5)[0]

    #一番確率の高い犬種と確率値を変数に代入
    pred_ans = decode_results[0][1]
    pred_score = decode_results[0][2]

    #一番予測結果の高い犬種と確率をreturn
    return pred_ans, pred_score
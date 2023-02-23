const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

function insertzyouge(){
    var img = new Image();
    // canvasタグで描画したい画像URL
    img.src = "";
    // 画像の読み込みが終わってからcanvasに画像を描画
    img.onload = () => {
        // drawImage(img要素, x座標, ｙ座標)
        ctx.drawImage(img, 0, 0);
    };
}
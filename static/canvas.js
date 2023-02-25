const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

function insert_zyouge(){
    var img = new Image();
    img.src = "static/img/上下矢印.png";
    img.onload = () => {
        ctx.drawImage(img, 0, 0);
    };
}

function insert_sayu(){
    var img = new Image();
    img.src = "static/img/左右矢印.png";
    img.onload = () => {
        ctx.drawImage(img, 0, 0);
    };
}

document.getElementById('image').appendChild(canvas);
const img = new Image();
img.src = 'static/img/上下矢印.png';
img.crossOrigin = 'anonymous';

img.onload = () => {
  // Canvasを画像のサイズに合わせる
  canvas.height = img.height;
  canvas.width  = img.width;

  // Canvasに描画する
  ctx.drawImage(img, 0, 0);
};

img.onerror = () => {
  console.log('画像の読み込み失敗');
};

/** ドラッグで移動 */
// ドラッグ状態かどうか
let isDragging = false;
// ドラッグ開始位置
let start = {
  x: 0,
  y: 0
};
// ドラッグ中の位置
let diff = {
  x: 0,
  y: 0
};
// ドラッグ終了後の位置
let end = {
  x: 0,
  y: 0
}
const redraw = () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(img, diff.x, diff.y)
};
canvas.addEventListener('mousedown', event => {
  isDragging = true;
  start.x = event.clientX;
  start.y = event.clientY;
});
canvas.addEventListener('mousemove', event => {
  if (isDragging) {
    diff.x = (event.clientX - start.x) + end.x;
    diff.y = (event.clientY - start.y) + end.y;
    redraw();
  }
});
canvas.addEventListener('mouseup', event => {
  isDragging = false;
  end.x = diff.x;
  end.y = diff.y;
});
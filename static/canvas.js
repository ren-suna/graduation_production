const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

function insert_zyouge(){
    var img = new Image();
    img.src = "static\img\上下矢印.png";
    img.onload = () => {
        ctx.drawImage(img, 0, 0);
    };
}




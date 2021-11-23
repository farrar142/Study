var Body = {
    setColor:function (color) {
        document.querySelector('body').style.color = color;            
    },
    setBgColor:function (bgcolor) {
        document.querySelector('body').style.backgroundColor = bgcolor;
    }
}

var Links = {
    setColor:function(color){
        var alist = document.querySelectorAll('a');
        var i = 0;

        while(i < alist.length) {
            alist[i].style.color = color;
            i = i + 1;
        }
    }

}

function night_day_handler(self){



    if (self.value==='Night'){
        Body.setColor('white');
        Body.setBgColor('black');
        self.value='Day';
        Links.setColor('powderblue');
    }else{
        Body.setColor('black')
        Body.setBgColor('white')
        self.value='Night';
        Links.setColor('black');
    }
}


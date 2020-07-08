function hamburgerBtn() {
    const DOM ={
        hamLogo: document.querySelector('.ham-stripes'),
        lineTop: document.querySelector('.line2'),
        lineMiddle: document.querySelector('.line1'),
        lineBot: document.querySelector('.line3'),
        hamburgerCover: document.querySelector('.hamburger-cover'),
        sections: document.querySelectorAll('section'),
        footer: document.querySelector('footer'),
        nav: document.querySelector('nav'),
    }

    var browserWidth = '';

    function adjustCover(){
        // Hide / Show all content 
        DOM.sections.forEach((e)=>{
            e.classList.toggle('display-off');
        });
        DOM.footer.classList.toggle('display-off');
         
        // Hamburger stripe animation
        DOM.lineMiddle.classList.toggle('line-middle-on');
        DOM.lineTop.classList.toggle('line-top-on');
        DOM.lineBot.classList.toggle('line-bot-on');
        
        // Show / Hide hamburger cover
        DOM.hamburgerCover.classList.toggle('display-off');
        DOM.hamburgerCover.classList.toggle('on');  
    }

    DOM.hamLogo.addEventListener('click', ()=>{ 
        browserWidth = window.innerWidth;
        /* Make hamburger cover width the same as content width 
        to stop navbar from resizing when hamburger cover is open */ 
        let contentWidth = DOM.sections[0].offsetWidth;
        DOM.hamburgerCover.style.width = `${contentWidth}px`;

        adjustCover();
        
    });

    function hideCoverOnResize(){
        if(DOM.hamburgerCover.classList.contains('on')){
            if (browserWidth != window.innerWidth){
               adjustCover();
            }
        }
    }

    window.addEventListener('resize', hideCoverOnResize);
}

try {
    hamburgerBtn();
}
catch(err) {
    console.log(err);
}

function calculator() {

    let DOM = {
            webCalculator: document.querySelector('.web-calculator'),
            eshopCalculator: document.querySelector('.eshop-calculator'),
            designCalculator: document.querySelector('.design-calculator'),
            webForm: document.querySelector('.web'),
            webFinal: document.querySelector('#web-form-final'),
            eshopForm: document.querySelector('.eshop'),             
            eshopFinal: document.querySelector('#eshop-form-final'),
            designForm: document.querySelector('.design'),
            designFinal: document.querySelector('#design-form-final'),
            webBtn: document.querySelector('.web-redirect-btn'),
            eshopBtn: document.querySelector('.eshop-redirect-btn'),
            designBtn: document.querySelector('.design-redirect-btn'),
            wRedirectBtn: document.querySelector('#w-btn'),
            eRedirectBtn: document.querySelector('#e-btn'),
            dRedirectBtn: document.querySelector('#d-btn'),
            webConfirmForm: document.querySelector('.web-final-form'),
            eshopConfirmForm: document.querySelector('.eshop-final-form'),
            designConfirmForm: document.querySelector('.design-final-form'),
            calcForm: document.querySelector('.calc-form'),
            eCalcForm: document.querySelector('.e-calc-form'),
            dCalcForm: document.querySelector('.d-calc-form'),
            finalFormBtn: document.querySelector('#hidden-form-btn'),
            eshopFinalFormBtn: document.querySelector('#e-hidden-form-btn'),
            designFinalFormBtn: document.querySelector('#d-hidden-form-btn'),
            webCheckedBox: document.querySelectorAll('.web-checked'),
            eshopCheckedBox: document.querySelectorAll('.eshop-checked'),
            designCheckedBox: document.querySelectorAll('.design-checked'),
            mSwitch: document.querySelectorAll('.m-switch'), 
            dSwitch: document.querySelectorAll('.d-switch'),
            calculatorItems: document.querySelectorAll('.calc-items'),
            selectBox: document.querySelectorAll('.select')
    }

    DOM.selectBox.forEach(e=>{
        e.options[0].disabled=true;
    });

    function expandCalculator(){
        /*  
            on click expand targeted calculator and turn on green switch, close 
            others if was opened
        */ 
        let calcItems = []
        let switchBulbs = []
        DOM.mSwitch.forEach(function(e) {

            // Get list of all calculators
            calcItems.push(e.parentNode.nextElementSibling);

            // Get list of all bulbs
            switchBulbs.push(e);

            e.addEventListener('click', ()=>{
                
                let currentSwitch = e;
                let currentCalcItem = e.parentNode.nextElementSibling;
    
                currentCalcItem.classList.toggle('m-flag');
                
                // Turn on green light on click
                if(!e.classList.contains('switch-light')){
                    e.classList.add('switch-light');
                }
                else if(e.classList.contains('switch-light')){
                    e.classList.remove('switch-light');
                }

                // open one, close others
                calcItems.forEach(e => {
                    if(currentCalcItem !=e && !e.classList.contains('m-flag')){
                        e.classList.add('m-flag');
                    }
                })

                // lit one, extinguish others
                switchBulbs.forEach(e => {
                    if(currentSwitch !=e && e.classList.contains('switch-light')){
                        e.classList.remove('switch-light');
                    }
                })

                
                // show redirect button
                let redirectBtn = e.parentNode.nextElementSibling.children[3];
                redirectBtn.classList.remove('display-off');

                // if redirect button is hidden, show
                if(redirectBtn.classList.contains('d-flag')){
                    redirectBtn.classList.remove('d-flag');
                }
                
                else if(!redirectBtn.classList.contains('d-flag')){
                    redirectBtn.classList.add('d-flag');
                }

                // show current btn, hide others
                calcItems.forEach(e => {
                    if(redirectBtn != e.childNodes[7] && !e.childNodes[7].classList.contains('d-flag')){
                        e.childNodes[7].classList.add('d-flag');
                    }
                });

                redirectBtn.addEventListener('click', function(){
                    currentSwitch.classList.add('display-off');
                });

                closeWebForm(currentSwitch, redirectBtn);
                closeEshopForm(currentSwitch, redirectBtn);
                closeDesignForm(currentSwitch, redirectBtn);

            });
        });
    }
    
    function setDefaultPrice(formCheckBoxes, output){
        let defaultPrice = 0;
        formCheckBoxes.forEach(element => {
            defaultPrice += parseInt(element.value);
            element.disabled = true;
        });
        defaultPrice += '€';
        output.innerHTML = defaultPrice;
    }

    setDefaultPrice(DOM.webCheckedBox, DOM.webFinal);
    setDefaultPrice(DOM.eshopCheckedBox, DOM.eshopFinal);
    setDefaultPrice(DOM.designCheckedBox, DOM.designFinal);

    function closeWebForm(bulb=null, rBtn=null){
        DOM.finalFormBtn.addEventListener('click', ()=>{

            // Hide final form of individual calculator
            DOM.webConfirmForm.classList.remove('web-confirm-form');
            DOM.webConfirmForm.classList.add('display-off');

            // Display calculator first form
            DOM.webCalculator.classList.remove('expand');
            DOM.webForm.classList.remove('display-off');
            
            // Add grid property for layout
            DOM.webForm.classList.add('web-form');

            // display other calculators
            DOM.eshopCalculator.classList.remove('display-off');
            DOM.designCalculator.classList.remove('display-off');
            //close green button
            bulb.classList.remove('display-off');
            rBtn.classList.remove('display-off');
        });
    }
    function closeEshopForm(bulb=null, rBtn=null){
        DOM.eshopFinalFormBtn.addEventListener('click', ()=>{

            // Hide final form of individual calculator
            DOM.eshopConfirmForm.classList.remove('web-confirm-form');
            DOM.eshopConfirmForm.classList.add('display-off');

            // Display calculator first form
            DOM.eshopCalculator.classList.remove('expand');
            DOM.eshopForm.classList.remove('display-off');
            
            // Add grid property for layout
            DOM.eshopForm.classList.add('eshop-form');

            // display other calculators
            DOM.webCalculator.classList.remove('display-off');
            DOM.designCalculator.classList.remove('display-off');

            //close green button
            bulb.classList.remove('display-off');
            rBtn.classList.remove('display-off');
        });
    }
    function closeDesignForm(bulb=null,rBtn=null){
        DOM.designFinalFormBtn.addEventListener('click', ()=>{

            // Hide final form of individual calculator
            DOM.designConfirmForm.classList.remove('web-confirm-form');
            DOM.designConfirmForm.classList.add('display-off');

            // Display calculator first form
            DOM.designCalculator.classList.remove('expand');
            DOM.designForm.classList.remove('display-off');
            
            // Add grid property for layout
            DOM.designForm.classList.add('design-form');

            // display other calculators
            DOM.webCalculator.classList.remove('display-off');
            DOM.eshopCalculator.classList.remove('display-off');

            //close green button
            bulb.classList.remove('display-off');
            rBtn.classList.remove('display-off');
        });
    }

    function getValues(node, parent) {
            let elements = [] 
            for(let i = 0; i<parent.children.length;i++) {
                elements.push(parent.children[i]);
            }        
            return elements; 
    }

    function filterPrices(valueArr, curr) {
            let total = 0;
            let selectTotal = 0;
        
            valueArr.forEach(e => {

                //Capture checked checkboxes values
                if(e.checked === true) {
                   let addedPrice = parseInt(e.value);
                   total += addedPrice;
                }

                //Capture selected option values
                if(e.className === 'select') {
                   let selectValue = parseInt(e.value);
                   if(isNaN(selectValue)){
                        if(isNaN(selectValue) || selectTotal === undefined){
                            selectValue = 0;
                        }
                   }
                   selectTotal += selectValue;
                }
            });
            return [total, selectTotal];
    }
   

    function activateForm(form, output, selectBox){
       
        form.addEventListener('click', function(e){

            //target clicked node
            let currentNode = e.target;
            let finalOutput = 0;

            if(currentNode.className === 'price' || currentNode.localName === 'option' || currentNode.className === 'select') { 
                /* 
                    localName for mozzila, edge, etc.
                    className for chrome, opera, etc..
                */ 

                //capture all sibling node values
                let formValues = getValues(currentNode, form);
                
                //produce a total price value
                let [totalPrice, selectTotal] = filterPrices(formValues, currentNode);
                
                //output price
                finalOutput = totalPrice + selectTotal;
                output.innerHTML = `${finalOutput}` + '€';
    
                //reset values
                boxValues = []
                totalPrice = 0 
            }
        });
    }
    
    function activateExtForm(btn){
        
        btn.addEventListener('click', function(e){
            
            switch(btn){
                case DOM.wRedirectBtn:
                    
                    // Hide first form
                    DOM.webForm.classList.toggle('web-form');
                    DOM.webForm.classList.toggle('display-off');

                    // Display final form
                    DOM.webConfirmForm.classList.toggle('display-off');
                    DOM.webConfirmForm.classList.toggle('web-confirm-form');

                    // Hide redirect button on final form
                    DOM.webBtn.classList.add('display-off');

                    // Expand form frame to take 3 columns
                    DOM.webCalculator.classList.toggle('expand');
                    
                    // Disable other calculators
                    DOM.eshopCalculator.classList.add('display-off');
                    DOM.designCalculator.classList.add('display-off');

                    // Add sliding animation
                    DOM.calcForm.classList.add('expand-animation');
                    setTimeout(()=>{
                        // Remove animation after its done, so it can be repeated as many times as clicked
                        DOM.calcForm.classList.remove('expand-animation');
                    }, 550);
                    
                    
                    break;

                case DOM.eRedirectBtn:
                    
                    // Hide first form
                    DOM.eshopForm.classList.toggle('eshop-form');
                    DOM.eshopForm.classList.toggle('display-off');
                   
                    // Display final form
                    DOM.eshopConfirmForm.classList.toggle('display-off');
                    DOM.eshopConfirmForm.classList.toggle('web-confirm-form');

                    // Hide redirect button on final form
                    DOM.eshopBtn.classList.add('display-off');

                    // Expand form frame to take 3 columns
                    DOM.eshopCalculator.classList.toggle('expand');

                    // Disable other calculators
                    DOM.webCalculator.classList.add('display-off');
                    DOM.designCalculator.classList.add('display-off');
                    
                    // Add sliding animation
                    DOM.eCalcForm.classList.add('expand-animation');
                    setTimeout(()=>{
                        // Remove animation after its done, so it can be repeated as many times as clicked
                        DOM.eCalcForm.classList.remove('expand-animation');
                    }, 550);

                    break;

                case DOM.dRedirectBtn:
                   
                    
                    // Hide first form
                    DOM.designForm.classList.toggle('design-form');
                    DOM.designForm.classList.toggle('display-off');
                   
                    // Display final form
                    DOM.designConfirmForm.classList.toggle('display-off');
                    DOM.designConfirmForm.classList.toggle('web-confirm-form');

                    // Hide redirect button on final form
                    DOM.designBtn.classList.add('display-off');

                    // Expand form frame to take 3 columns
                    DOM.designCalculator.classList.toggle('expand');

                    // Disable other calculators
                    DOM.webCalculator.classList.add('display-off');
                    DOM.eshopCalculator.classList.add('display-off');
                    
                    // Add sliding animation
                    DOM.dCalcForm.classList.add('expand-animation');
                    setTimeout(()=>{
                        // Remove animation after its done, so it can be repeated as many times as clicked
                        DOM.dCalcForm.classList.remove('expand-animation');
                    }, 550);
                   
                    break;
                default:
                    break;
                
            }
            
        })
    }

    expandCalculator();

    activateForm(DOM.webForm, DOM.webFinal);
    activateForm(DOM.eshopForm, DOM.eshopFinal);
    activateForm(DOM.designForm, DOM.designFinal);

    activateExtForm(DOM.wRedirectBtn);
    activateExtForm(DOM.eRedirectBtn);
    activateExtForm(DOM.dRedirectBtn);
}

try {
    calculator();}
catch(err){
    console.log(err);
}

function imageSwitcher() {
    const DOM = {
        imageHolder: document.querySelector('.portfolio-img-holder'),
        switchToL: document.querySelector('.p-btn-larrow'),
        switchToR: document.querySelector('.p-btn-rarrow'),
   }

    // Enable first image
    firstImage = DOM.imageHolder.children[0]
    firstImage.classList.remove('display-off');
    // Remove left button
    DOM.switchToL.classList.add('display-off');

    //capture current position
    current = firstImage;

    document.addEventListener('click', e =>{
        //capture left and right positions from current
        previousImg = current.previousElementSibling;
        nextImg = current.nextElementSibling;

        if (e.target.matches('.p-btn-larrow')){

            DOM.switchToR.classList.remove('display-off')
            current = previousImg;

            if(current.previousElementSibling === null) {
                DOM.switchToL.classList.add('display-off');
            }

            current.classList.remove('display-off');
            current.nextElementSibling.classList.add('display-off');
        }

        if (e.target.matches('.p-btn-rarrow')){ 

            DOM.switchToL.classList.remove('display-off')
            current = nextImg;
            
            if(current.nextElementSibling === null){
                DOM.switchToR.classList.add('display-off');
            }  

            current.previousElementSibling.classList.add('display-off');
            current.classList.remove('display-off');       
        }      
    });

}

try {
    imageSwitcher();
}
catch(err){
    console.log(err);
}
//ensure doesn't run in ifram
if (window.top === window) {
    
    //find window width and return to global.html
    var returnWidth = function(message) {
        
        //ensure correct message passed
        if (message.name === 'getIndicatorWidth') {
            var width = window.outerWidth;
            safari.self.tab.dispatchMessage( 'setIndicatorWidth', width );
        } 
    };

    //listen for message from global.html
    safari.self.addEventListener('message', returnWidth, false);
}

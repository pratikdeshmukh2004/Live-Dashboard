    $(document).ready(function() {
        var socket = io.connect();
        var audio = new Audio('https://github.com/pratikdeshmukh2004/Audio-Player/blob/master/message.mp3?raw=true')
        socket.on('connect', function() {
            socket.emit('connected');
            $('#myName').val('');
            $('#myMessage').val('');
        });

        socket.on('message', function(msg) {
            audio.play()
            var name = msg.json_data.name;
            var content = msg.json_data.content;
            var image = msg.json_data.image;
            console.log(msg.json_data);
            $(".special-items").prepend("<li class=\"special\">\n"+
            "<div class=\"thumb\">\n"+
                "<img width='250px' height='150px' src=\""+image+"\">/"+
            "</div>"+
            "<div class=\"desc\" style=\"float: left;\">"+
                "<div class=\"text text-white\">"+name+"</div>"+
                "<div class=\"subtext\">"+content+"</div>"+
            "</div>"+
        "</li>")
            console.log('Received message');
        });

        $('#sendButton').on('click', function() {
            var name = $('#myName').val();
            var content = $('#myContent').val();
            var image = $('#myImage').val();
            socket.send({name : name, content : content, image: image});
            $('#myName').val('');
            $('#myContent').val('');
            $('#myImage').val('');
        });

        socket.on('page_view_increase', function(count) {
        	console.log('ping');
			var total_count = count.page_views;
			console.log(total_count + ' views');
        	$("#pageViews").text(total_count);
		})
    });
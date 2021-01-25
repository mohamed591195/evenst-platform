var nextEventsURL;

function pullAndDisplayEvents() {
    data = {}

    switch (window.location.pathname) {
        case '/my-events/':
            data = { requestOwned: true };
            break;
        case '/joined-events/':
            data = { requestJoined: true };
    }

    $.ajax({
        type: 'GET',
        url: nextEventsURL || '/events-serialized/',
        data,
        success: data => {
            nextEventsURL = data.next;
            displayEvents(data.results)
        },
        error: (err) => console.log(err)
    })
}

$(document).ready(function () {
    pullAndDisplayEvents();

    let win = $(window)
    win.scroll(function () {
        if ($(document).height() - win.height() == win.scrollTop()) {
            pullAndDisplayEvents()
        };
    })
})


$('.event-list').on('click', '.attendance-btn', function () {

    var btn = $(this);
    btn.prop('disabled', true)

    $.ajax({

        url: '/attend-event/',

        type: 'POST',

        data: {
            eventId: btn.data('id')
        },

        success: data => {

            console.log(data)

            let dataSwitcher = {
                removed: 'attend',
                added: 'cancel attendance'
            }

            btn.html(dataSwitcher[data.action])
            btn.prop('disabled', false)
        },

        error: err => {
            console.log(err)
        }
    })
})

function displayEventAction(event) {
    if (event.participants.includes(currentUser.id)) {
        return 'cancel attendance';
    }
    return 'attend';
}

function displayEvents(events) {
    let eventsList = $('.event-list');

    events.forEach(event => {

        if (currentUser) {

            eventsList.append(`
            <div class="event-item" data-id=${event.id}>
                <h5>${event.title}</h5>
                <p class="date-time">
                   -> Holding Date: ${event.date}
                </p>
                <p> -> ${event.participants_count} attendants</p>
                <p> -> Owner: ${event.owner}</p>
                ${currentUser.email != event.owner ?
                    `<button data-id=${event.id} class="attendance-btn"> ${displayEventAction(event)} </button>` : 
                    `<span><a href="/edit-event/${event.id}/">Edit Event</a></span>`
                }      
            </div>   
        `) 
        }
        else {
            eventsList.append(`
            <div class="event-item" data-id=${event.id}>
                <h5>${event.title}</h5>
                <p class="date-time">
                   -> Holding Date: ${event.date}
                </p>
                <p> -> ${event.participants_count} attendants</p>
                <p> -> Owner: ${event.owner}</p>     
            </div>   
        `) 
        }
        
    });
}


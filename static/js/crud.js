let categories = null;
let difficulties = null;
let search_text = null;
let limit = 5;


$(document).ready(() => {
    init_filters();

    const table = init_table();

    add_event_handlers(table);
    onClickRow(table);
});

const init_table = () => {
    return $('#questions-table').DataTable( {
        cache: false,
        ajax: {
            url: '/api/v1/questions',
            cache: false,
            dataSrc: function(data) {
                if(data.results) {
                    return data.results.map(item => {
                        return {
                        'id': item.id,
                        'question': item.question,
                        'difficulty': item.difficulty === '2' ? 'difficult' : item.difficulty === '1' ? 'medium' : 'easy',
                        'category': item.category.title
                    }
                    });
                }else{
                    return [];
                }
            },
        },
        searching: false,
        paging: false,
        processing: true,
        columns: [
            {'data': 'id'},
            {'data': 'question'},
            {'data': 'difficulty'},
            {'data': 'category'},
        ]
    } );
}

const init_filters = () => {
    $('#categories').select2({
        ajax: {
            url: '/api/v1/categories',
            processResults: function (data) {
                // Transforms the top-level key of the response object from 'items' to 'results'
                return {
                    results: data.map(item => ({'id': item.id, 'text': item.title}))
                }
            }
        }
    });

    $('#difficulty').select2();
};

const add_event_handlers = (table) => {
  $('#categories').on('change', event => {
      categories = $('#categories').val();
      ajax(table);
  });

  $('#difficulty').on('change', event => {
      difficulties = $('#difficulty').val();
      ajax(table);
  });

  $('#search-text').on('input', event => {
      search_text = $('#search-text').val();
      ajax(table);
  });

  $('#limit').on('input', event => {
      limit = $('#limit').val();
      $('#limit-val').val(limit);
      ajax(table);
  });
};

const ajax = (table) => {
    const params = {};
    if(categories && categories.length > 0){
        params['category'] = categories;
    }
    if(difficulties && difficulties.length > 0){
        params['difficulty'] = difficulties;
    }
    if(search_text && search_text.length > 0 && search_text !== "" && search_text !== " "){
        params['search'] = search_text;
    }

    if(limit){
        params['limit'] = limit;
    }

    const paramString = new URLSearchParams(params);

    table.ajax.url('/api/v1/questions/' + '?' + paramString.toString());
    table.ajax.reload();
};

const onClickRow = (table) => {
    $('#questions-table').on('click', 'tbody tr',  function() {
        const row = table.row(this).data();
        window.location.href("/questions/" + row['id']);
    });
}


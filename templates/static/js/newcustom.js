$("#submitit").click(function () {
        $.ajax({
            data:JSON.stringify( {
                name: $("input[name='univname']").value,
                country: $('#country').value,
                quant: $('#quant').value,
                verbal: $('#verbal').value,
                toefl: $('#toefl').value,
                ielts: $('#ielts').value,
                deadlines: $('#deadlines').value
            }),
            content_type:
            type: 'POST',
            url: '/form2'
        })
            .done(function (data) {
                var exec = "<table> <tr><th>University Name</th><th>Country</th><th>GRE Quant</th><th>GRE Verbal</th><th>TOEFL</th> <th>IELTS</th> <th>Specifics</th><th>Deadline</th></tr>"
                for (var i = 0; i < data.namess.length; i++) {
                    exec = exec + "<tr>";
                    exec = exec + "<td>" + data.namess[i] + "</td>" + "<td>" + data.countrys[i] + "</td>" + "<td>" + data.quants[i] + "</td>" + "<td>" + data.verbals[i] + "</td>" + "<td>" + data.toefls[i] + "</td>" + "<td>" + data.ieltss[i] + "</td>" + "<td>" + data.specifics[i] + "<td>" + data.deadlinee[i] + "</td>";
                    exec = exec + "</tr>";
                }

            })


    });

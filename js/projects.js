var table1;
var table2;
var table3;
var searchValue1 = '';
var searchValue2 = '';
var searchValue3 = '';
var selectValues1 = [];
var selectValues2 = [];
var selectValues3 = [];

$(document).ready(function() {
    table1 = $('#dataTable1').DataTable({
        "ordering":  true,
        "paging":    false,
        "info":      false,
        "searching": true
    });
    
    table2 = $('#dataTable2').DataTable({
        "ordering":  true,
        "paging":    false,
        "info":      false,
        "searching": true
    });

    table3 = $('#dataTable3').DataTable({
        "ordering":  true,
        "paging":    false,
        "info":      false,
        "searching": true
    });

    // Store value in first table's search box before searching
    $('#table_search1').keyup(function(e) {
        searchValue1 = $(this).val();
        tableSearch(1);
    });

    // Store value in second table's search box before searching
    $('#table_search2').keyup(function(e) {
        searchValue2 = $(this).val();
        tableSearch(2);
    });

    // Store value in third table's search box before searching
    $('#table_search3').keyup(function(e) {
        searchValue3 = $(this).val();
        tableSearch(3);
    });
});

/*
 * Given a table number, perform a smart search in that table
 * using the combined values of its search box and taxonomy drop-downs.
 */
function tableSearch(tableNum) {
    let filterStr = "";
    switch(tableNum) {
        case 1:
            filterStr = searchValue1 + ' ' + selectValues1.join(' ');
            table1.search(filterStr).draw();
            break;
        case 2:
            filterStr = searchValue2 + ' ' + selectValues2.join(' ');
            table2.search(filterStr).draw();
            break;
        case 3:
            filterStr = searchValue3 + ' ' + selectValues3.join(' ');
            table3.search(filterStr).draw();
            break;
        default:
            // Error, exit function
            console.error("Invalid table number found: " + tableNum);
            return;
    }
}

/*
 * Given the ID of a select drop-down, determine which table it belongs to 
 * by checking if it ends in "1" or "2", then collect all the defined values
 * of the selects for that table and filter the table using them.
 */
function updateTaxonomyFilters(id) {
    let tableNum = id.slice(-1);

    if (!(tableNum == "1" || tableNum == "2" || tableNum == "3")) {
        // Error, exit function
        console.error("Invalid table number found: " + tableNum);
        return;
    }

    let scienceArea = document.getElementById("tax_cat_1_" + tableNum).value;
    let functionality = document.getElementById("tax_cat_2_" + tableNum).value;
    let span = document.getElementById("tax_cat_3_" + tableNum).value;
    let inputOutputFormats = document.getElementById("tax_cat_4_" + tableNum).value;
    let inputSources = document.getElementById("tax_cat_5_" + tableNum).value;
    let intent = document.getElementById("tax_cat_6_" + tableNum).value;

    let selectValues = [scienceArea, functionality, span, inputOutputFormats, inputSources, intent];

    switch(tableNum) {
        case "1":
            // Store non-empty select values for first table before searching
            selectValues1 = selectValues.filter(function (v) { return v !== ''; });
            tableSearch(1);
            break;
        case "2":
            // Store non-empty select values for second table before searching
            selectValues2 = selectValues.filter(function (v) { return v !== ''; });
            tableSearch(2);
            break;
        case "3":
            // Store non-empty select values for third table before searching
            selectValues3 = selectValues.filter(function (v) { return v !== ''; });
            tableSearch(3);
            break;
    }
}

/*
 * Show/hide taxonomy drop-down filters for the appropriate table.
 */ 
function toggleFilters(id) {
    let tableNum = id.slice(-1);

    if (!(tableNum == "1" || tableNum == "2" || tableNum == "3")) {
        // Error, exit function
        console.error("Invalid table number found: " + tableNum);
        return;
    }

    $filters = $("#taxonomy-filters" + tableNum);
    $button = $("#filter-toggle" + tableNum);
    $filters.slideToggle(300, function () {
        $button.text(function () {
            return $filters.is(":visible") ? "Hide Keyword Filters" : "Show Keyword Filters";
        });
    });
}

/*
 * Pretty print the given keyword for display.
 */
function prettyPrintKeyword(keyword) {
    switch(keyword) {
        //special replacements
        case "ionosphere_thermosphere_mesosphere":
            return "Ionosphere/Thermosphere/Mesosphere";
        case "netcdf":
            return "NetCDF";
        //all caps replacements
        case "fits":
        case "cdf":
        case "ascii":
        case "idl_save":
        case "hdf5":
        case "csv":
            return keyword.toUpperCase().replace("_", " ");
        //capital first letter replacements
        default:
            return keyword
                .split('_')
                .map(function(word) {
                    return word[0].toUpperCase() + word.substr(1);
                })
                .join(' ');
    }
}

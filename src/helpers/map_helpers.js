let mapHelpers = {};

//constants

//swiss indicators
mapHelpers.swiss_solar = 0.054933;
mapHelpers.swiss_population = 8606033;
mapHelpers.swiss_car = 0.017949;
mapHelpers.swiss_heating = 0.326350;

//map dimensions
mapHelpers.width = 600;
mapHelpers.rect_width = mapHelpers.width * 900 / 700;

//colors of map
mapHelpers.canton_color = 'rgb(0,128,0)' //green !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.commune_color = "rgb(255,165,0)" //orange !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.commune_selected_color = "rgb(255,0,0)" //red !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.canton_stroke = "rgb(0,0,0)" //black !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.commune_stroke = "rgb(0,0,0)" //black !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.canton_stroke_width = 1
mapHelpers.commune_stroke_width = 0.5
mapHelpers.canton_color_mouse_on = "rgb(144,238,144)" // !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.commune_color_mouse_on = "rgb(255,204,153)" // !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.commune_selected_color_mouse_on = "rgb(255,105,97)" // !!!! colors must be in rgb and not just name of color (to compare colors)
mapHelpers.rect_background_color = "#ffffff"

//


// ################################FUNCTIONS###########################################

/**
    Calculate how much a canton contributes to the country's total statistic and how much a commune contributes to the canton's total statistic
    * @param dataset data of statistic we are computing on
*/
mapHelpers.calculatePercentageContribution = (dataset) => {
    console.log('labels', dataset.labels)
    return {
        labels: ['Swiss %', 'Canton %'].map(x => dataset.labels[0] + ' ' + x),
        country: { data: [1, null], label: dataset.country.label, population: dataset.country.population },
        canton: {
            data: [
                (dataset.canton.data[0] === null ?
                    null :
                    dataset.canton.data[0] * dataset.canton.population / (dataset.country.population * dataset.country.data[0])),
                dataset.canton.data[0] === null ? null : 1
            ],
            label: dataset.canton.label,
            population: dataset.canton.population
        },
        commune: {
            data: [
                (dataset.commune.data[0] === null ?
                    null :
                    dataset.commune.data[0] * dataset.commune.population / (dataset.country.population * dataset.country.data[0])),
                (dataset.commune.data[0] === null ?
                    null :
                    dataset.commune.data[0] * dataset.commune.population / (dataset.canton.population * dataset.canton.data[0]))
            ],
            label: dataset.commune.label,
            population: dataset.commune.population
        }
    }
};


mapHelpers.selectProvince = (that, province) => {
    that.province = province;
};
mapHelpers.openInfo = (that, province) => {
    that.currentProvince = province;
};
mapHelpers.closeInfo = (that) => {
    that.currentProvince = '';
};
/**
    determines if a statistic is none or not
*/
mapHelpers.not_valid_statistic = (stat) => {
    return stat == 'null'
};
/**
    gets the latest sustainability indicators of a region
    @param region region we selected
*/
mapHelpers.get_latest_energy_data = (region) => {

    //data is in a string and seperated in by ' '
    let electric_car_share_time_series = region.electric_car_share.split(' ')

    //get latest indicator
    var el_car_share_most_recent = electric_car_share_time_series[electric_car_share_time_series.length - 1]

    //check if it's a valid statistic

    if (mapHelpers.not_valid_statistic(el_car_share_most_recent))
        el_car_share_most_recent = null

    //data is in a string and seperated in by ' '
    let renewable_heating_share_time_series = region.renewable_heating_share.split(' ')

    //get latest indicator
    var ren_heat_share_most_recent = renewable_heating_share_time_series[renewable_heating_share_time_series.length - 1]

    //check if it's a valid statistic
    if (mapHelpers.not_valid_statistic(ren_heat_share_most_recent))
        ren_heat_share_most_recent = null

    //data is in a string and seperated in by ' '
    let solar_potential_usage_time_series = region.solar_potential_usage.split(' ')

    //get latest indicator
    var sol_pot_usage_most_recent = solar_potential_usage_time_series[solar_potential_usage_time_series.length - 1]

    //check if it's a valid statistic
    if (mapHelpers.not_valid_statistic(sol_pot_usage_most_recent))
        sol_pot_usage_most_recent = null

    return {
        heating: { data: [ren_heat_share_most_recent], label: region.name, population: region.population },
        solar: { data: [sol_pot_usage_most_recent], label: region.name, population: region.population },
        electric_car: { data: [el_car_share_most_recent], label: region.name, population: region.population }
    }
}

/**
    change canton data given to bar plot
    @param canton_data data we want to add
*/
mapHelpers.change_bar_plot_canton_data = (that, canton_data) => {

    //change canton data on bar plot (if nothing is stated set everything to null)
    if (canton_data == null) {
        that.energyData_solar.canton = that.default_canton_energy_data
        that.energyData_heating.canton = that.default_canton_energy_data
        that.energyData_car.canton = that.default_canton_energy_data
    } else {
        that.energyData_solar.canton = canton_data.solar
        that.energyData_heating.canton = canton_data.heating
        that.energyData_car.canton = canton_data.electric_car
    }

    that.energy_Data_heating_perc_contr = mapHelpers.calculatePercentageContribution(that.energyData_heating)

    that.energyData_car_perc_contr = mapHelpers.calculatePercentageContribution(that.energyData_car)

    that.energyData_solar_perc_contr = mapHelpers.calculatePercentageContribution(that.energyData_solar)
}

/**
    change commune data given to bar plot
    @param commune_data data we want to add
*/
mapHelpers.change_bar_plot_commune_data = (that, commune_data = null) => {
    //change canton data on bar plot (if nothing is stated set everything to null)
    if (commune_data == null) {
        that.energyData_solar.commune = that.default_commune_energy_data
        that.energyData_heating.commune = that.default_commune_energy_data
        that.energyData_car.commune = that.default_commune_energy_data
    } else {
        that.energyData_solar.commune = commune_data.solar
        that.energyData_heating.commune = commune_data.heating
        that.energyData_car.commune = commune_data.electric_car
    }

    that.energy_Data_heating_perc_contr = mapHelpers.calculatePercentageContribution(that.energyData_heating)

    that.energyData_car_perc_contr = mapHelpers.calculatePercentageContribution(that.energyData_car)

    that.energyData_solar_perc_contr = mapHelpers.calculatePercentageContribution(that.energyData_solar)
}


export default mapHelpers;

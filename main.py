import data_processing as dp

def main():
    # Ejercicio 1.1
    filepath = 'Data/nics-firearm-background-checks.csv'
    df = dp.read_csv(filepath)

    # Ejercicio 1.2
    cleaned_df = dp.clean_csv(df)

    # Ejercicio 1.3
    renamed_df = dp.rename_col(cleaned_df)

    # Ejercicio 2.1
    date_split_df = dp.breakdown_date(renamed_df)

    # Ejercicio 2.2
    erasmon_df = dp.erase_month(date_split_df)

    # Ejercicio 3.1
    grouped_df = dp.groupby_state_and_year(erasmon_df)

    # Ejercicio 3.2
    dp.print_biggest_handguns(grouped_df)

    # Ejercicio 3.3
    dp.print_biggest_longguns(grouped_df)

     # Ejercicio 4.1
    dp.time_evolution(erasmon_df)

    # Ejercicio 5.1
    state_grouped_df = dp.groupby_state(grouped_df)

    # Ejercicio 5.2
    cleaned_states_df = dp.clean_states(state_grouped_df)

    # Ejercicio 5.3
    population_filepath = 'Data/us-state-populations.csv'
    merged_df = dp.merge_datasets(cleaned_states_df, population_filepath)

    # Ejercicio 5.4
    relative_values_df = dp.calculate_relative_values(merged_df)

    # Ejercicio 5.5
    dp.analyze_relative_values(relative_values_df)

    # Ejercicio 6: Generar mapas coropléticos
    dp.generate_choropleth_map(relative_values_df, 'permit_perc', 'permit_perc_map')
    dp.generate_choropleth_map(relative_values_df, 'handgun_perc', 'handgun_perc_map')
    dp.generate_choropleth_map(relative_values_df, 'longgun_perc', 'longgun_perc_map')


if __name__ == "__main__":
    main()

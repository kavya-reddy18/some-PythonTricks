from covid import Covid
covid=Covid()
print(covid.get_total_active_cases())
print(covid.get_total_deaths())
print(covid.get_total_confirmed_cases())
print(covid.get_status_by_country_name("india"))
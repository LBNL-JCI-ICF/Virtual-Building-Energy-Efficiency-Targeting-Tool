'''

Energy Efficiency Targeting Tool Copyright (c) 2018, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.

If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at  IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so. 

'''

import pandas as pd
import numpy as np


class Constants:
    # Unit conversions
    M3_to_kWh = 8.816  # m3 of Natural gas
    MWH_to_kWh = 1000
    MJ_to_kWh = 1000 / 3600
    GJ_to_kWh = 1000000 / 3600
    Btu_to_kWh = 0.000293071
    MMBtu_to_kWh = 293.071
    Therms_to_kWh = 29.307
    Decatherms_to_kWh = 293.071

    # Default fuel price
    electricity_unit_price = 0.1  # USD/kWh EIA
    fossil_fuel_unit_price = 0.025  # USD/kWh EIA

    # Constants
    earth_radius = 6371  # Radius of earth in kilometers. Use 3959 for miles
    days_in_year = 365
    rgb_color_strs = [
        "rgb(255, 87, 51)", "rgb(41, 128, 185)", "rgb(34, 153, 84)",
        "rgb(44, 62, 80)", "rgb(118, 68, 138)", "rgb(241, 196, 15)",
        "rgb(218, 247, 166)", "rgb(241, 15, 203)", "rgb(5, 249, 71)",
        "rgb(13, 13, 13)", "rgb(0, 0, 0)"
    ]

    # Default NOAA weather station lists
    # Weather station in the US
    d_us_weather_station = {
        'station_ID': [
            "619760-99999", "690150-93121", "700197-26558", "700632-26645",
            "700634-27408", "700635-26465", "700638-99999", "700860-27401",
            "701040-26631", "701043-26623", "701730-26535", "701748-99999",
            "701945-46405", "701995-26628", "702035-26704", "702040-26703",
            "702070-26627", "702084-26650", "702120-26646", "702185-26622",
            "702186-26651", "702223-26602", "702315-26536", "702320-26516",
            "702325-26443", "702350-26534", "702460-26512", "702595-26559",
            "702607-25378", "702626-99999", "702627-26561", "702645-46403",
            "702650-26407", "702685-27518", "702715-46407", "702720-26401",
            "702746-26497", "702756-26479", "703057-26653", "703059-99999",
            "703061-25521", "703330-25508", "703333-25518", "703334-25519",
            "703407-26553", "703430-25402", "703655-26552", "703855-25369",
            "703884-25376", "703926-99999", "703985-25377", "711680-99999",
            "720110-53983", "720113-54829", "720170-63851", "720172-53996",
            "720198-54813", "720257-63835", "720265-63833", "720267-23224",
            "720268-53882", "720269-12982", "720272-94282", "720273-12981",
            "720274-93799", "720276-12983", "720277-63843", "720286-53977",
            "720287-53967", "720289-63836", "720294-53898", "720295-53972",
            "720296-53945", "720298-53971", "720299-53966", "720301-63846",
            "720303-53973", "720304-64752", "720305-53964", "720307-63804",
            "720311-53962", "720314-93983", "720316-12984", "720318-53965",
            "720319-63841", "720323-93947", "720324-64753", "720328-63832",
            "720330-63853", "720340-54818", "720342-53947", "720343-54852",
            "720344-54920", "720345-94086", "720346-53991", "720347-63877",
            "720348-63886", "720351-54919", "720354-63901", "720356-13999",
            "720357-53993", "720358-53999", "720368-54924", "720371-54850",
            "720373-92824", "720374-92825", "720375-54844", "720376-63880",
            "720379-63882", "720381-63885", "722026-12826", "722031-63839",
            "722032-54916", "722041-12993", "722042-53978", "722044-53930",
            "722050-12815", "722055-12861", "722062-63842", "722071-53935",
            "722074-63840", "722076-94891", "722078-53938", "722079-53888",
            "722089-94959", "722091-53940", "722092-53941", "722094-53984",
            "722096-53127", "722098-64761", "722112-53982", "722113-53979",
            "722114-54901", "722120-12833", "722123-12809", "722128-53899",
            "722136-53883", "722143-53975", "722147-53817", "722152-53957",
            "722154-53885", "722158-99999", "722159-12980", "722164-53949",
            "722165-63808", "722172-63810", "722173-53951", "722174-23097",
            "722175-13860", "722177-63811", "722178-53953", "722187-93911",
            "722188-53985", "722192-23033", "722210-13858", "722216-99999",
            "722241-54925", "722252-54923", "722253-53992", "722256-64774",
            "722265-13821", "722270-13864", "722319-53943", "722329-12936",
            "722332-54953", "722336-99999", "722338-12994", "722342-54931",
            "722343-54826", "722346-54824", "722351-12953", "722362-93937",
            "722363-23098", "722403-12968", "722436-12906", "722485-13944",
            "722535-12909", "722536-12911", "722537-12961", "722552-93929",
            "722561-99999", "722563-53952", "722587-93955", "722637-93046",
            "722640-93035", "722666-93943", "722683-93083", "722693-93097",
            "722704-99999", "722721-93063", "722745-23109", "722785-23111",
            "722860-23119", "722866-99999", "722910-93116", "722925-93117",
            "722972-63878", "723030-13714", "723034-93747", "723046-13766",
            "723055-63816", "723062-99999", "723065-13783", "723066-13713",
            "723067-93726", "723069-93753", "723079-93796", "723083-13763",
            "723087-93735", "723122-63889", "723123-14886", "723126-99999",
            "723144-53890", "723146-53892", "723148-63859", "723156-63812",
            "723177-63807", "723408-13814", "723441-54921", "723449-53954",
            "723520-13902", "723540-13919", "723550-13945", "723625-93057",
            "723629-53998", "723654-93091", "723758-54928", "723759-53990",
            "723788-53135", "723810-23114", "723815-23161", "723825-23131",
            "723895-23149", "723930-93214", "724037-93728", "724056-63805",
            "724057-13701", "724058-53818", "724065-99999", "724077-54779",
            "724084-54760", "724088-13707", "724090-14780", "724096-14706",
            "724105-93760", "724107-53895", "724113-53881", "724127-53801",
            "724238-53886", "724285-13812", "724338-13802", "724354-63815",
            "724363-13803", "724365-53896", "724387-54807", "724454-93996",
            "724464-53916", "724467-13930", "724509-53939", "724550-13947",
            "724677-93007", "724680-94015", "724695-23036", "724836-23208",
            "724837-93216", "724946-93232", "724975-93809", "725014-54780",
            "725054-64710", "725058-94793", "725144-54723", "725155-94761",
            "725165-94737", "725175-64706", "725292-14976", "725335-94833",
            "725345-14834", "725373-54819", "725377-14804", "725383-54827",
            "725387-94899", "725405-54816", "725406-54817", "725415-54821",
            "725416-14864", "725417-54822", "725418-54823", "725453-14930",
            "725463-14966", "725473-94979", "725498-94998", "725512-14989",
            "725515-94947", "725556-94975", "725621-94063", "725624-14994",
            "725755-24101", "725810-24193", "725985-24267", "726077-14616",
            "726079-94601", "726130-14755", "726155-54736", "726165-94721",
            "726184-94709", "726190-94626", "726384-14817", "726395-14808",
            "726417-54911", "726418-54912", "726427-54908", "726436-94930",
            "726437-94940", "726464-54834", "726465-94890", "726466-54917",
            "726467-54909", "726468-54913", "726487-94896", "726507-54907",
            "726530-94943", "726539-94056", "726549-54905", "726554-54906",
            "726559-94976", "726561-94997", "726563-94969", "726572-94966",
            "726585-14954", "726586-94948", "726587-94927", "726589-94968",
            "726625-24006", "726627-94037", "726676-24087", "726764-94163",
            "726813-94195", "726815-24106", "726875-94107", "727130-14604",
            "727417-54825", "727430-94850", "727435-54820", "727445-94926",
            "727457-94962", "727458-94919", "727459-94964", "727473-94977",
            "727504-94999", "727507-54904", "727508-54915", "727550-14958",
            "727555-94956", "727573-94928", "727575-94925", "727675-94011",
            "727677-94041", "727684-94051", "727687-94028", "727760-99999",
            "727834-24136", "727855-24114", "727924-24223", "740030-24103",
            "742060-24207", "742078-64773", "742079-63876", "744652-53897",
            "744653-63814", "744656-53891", "744657-53887", "744658-53889",
            "744659-53822", "744662-63817", "744907-14753", "744910-14703",
            "745980-13702", "745985-63806", "746380-99999", "746710-13806",
            "746930-93737", "747320-23002", "747355-53997", "747686-13820",
            "747750-13846", "747804-13824", "747805-63818", "747806-63809",
            "747880-12810", "747900-13849", "747946-12886", "747950-12867",
            "785140-11603"
        ],
        'station_name': [
            "SERGE-FROLOW (ILE TROMELIN)", "TWENTY NINE PALMS", "SELAWIK",
            "BUCKLAND AIRPORT", "UGNU-KUPRAUK AIRPORT",
            "GALBRAITH LAKE AIRPORT", "FALSE PASS", "BARTER ISLAND AIRPORT",
            "CAPE LISBURNE LRRS AIRPORT", "POINT HOPE AIRPORT",
            "INDIAN MOUNTAIN LRRS ARPT", "PROSPECT CREEK AIRPORT",
            "ARCTIC VILLAGE AIRPORT", "CAPE DARBY REMOT COM OUTLT",
            "SAVOONGA AIRPORT", "GAMBELL AIRPORT", "UNALAKLEET AIRPORT",
            "EMMONAK", "CAPE ROMANZOF LRRS ARPT", "MEKORYUK AIRPORT",
            "HOOPER BAY AIRPORT", "KOYUK AIRPORT", "TATALINA LRRS AIRPORT",
            "ANIAK AIRPORT", "WASILLA AIRPORT", "SPARREVOHN LRRS AIRPORT",
            "MINCHUMINA", "SOLDOTNA AIRPORT", "HOONAH SEAPLANE BASE",
            "PILOT POINT", "RUBY  AIRPORT", "MCKINLEY NATIONAL PARK AIRPORT",
            "EIELSON AFB AIRPORT",
            "ATQASUK EDWARD BURNELL SR. MEMORIAL AIRPORT", "SKELTON AIRPORT",
            "ELMENDORF AFB AIRPORT", "BIRCHWOOD AIRPORT",
            "VALDEZ PIONEER FIELD AIRPORT", "TOKSOOK BAY AIRPORT", "KING COVE",
            "IGIUGIG AIRPORT", "PORT HEIDEN AIRPORT", "CHIGNIK AIRPORT",
            "EGEGIK AIRPORT", "SLEETMUTE AIRPORT",
            "MIDDLETON ISLAND METEOROLOGY RADAR SITE", "HUSLIA AIRPORT",
            "KAKE AIRPORT", "HYDABURG SEAPLANE BASE", "AKHIOK",
            "METLAKATLA SEAPLANE BASE", "SIOUX FALLS CLIMATE",
            "LLANO MUNICIPAL AIRPORT", "OAKLAND/TROY AIRPORT",
            "METROPOLIS MUNICIPAL AIRPORT",
            "MENA INTERMOUNTAIN MUNICIPAL AIRPORT", "MUNISING LAKESHORE",
            "EARLY COUNTY AIRPORT", "THOMAS C RUSSELL FLD ARPT",
            "AUBURN MUNICIPAL AIRPORT", "DCATR CO INDUS AIRPK ARPT",
            "BROOKS COUNTY AIRPORT", "SKAGIT REGIONAL AIRPORT",
            "BAY CITY MUNICIPAL AIRPORT", "COLUMBUS CO MUNICIPAL ARPT",
            "EDINBURG INTL AIRPORT", "SHELBY MUNICIPAL AIRPORT",
            "GRANBURY MUNICIPAL ARPT", "GRAYSON COUNTY AIRPORT",
            "THOMSON-MCDUFFIE CO ARPT", "WASHINGTON-WILKES CO ARPT",
            "HILLSBORO MUNICIPAL ARPT", "JASPER COUNTY-BELL FLD APT",
            "CHEROKEE COUNTY AIRPORT", "MID-WAY REGIONAL AIRPORT",
            "PLANTATION AIRPARK", "HEARNE MUNICIPAL AIRPORT",
            "WINGS FIELD AIRPORT", "DECATUR MUNICIPAL AIRPORT",
            "MADISON CO EXECUTIVE ARPT", "MOUNT PLEASANT RGNL ARPT",
            "PALESTINE MUNICIPAL ARPT", "NUECES COUNTY ARIPORT",
            "GRAHAM MUNICIPAL AIRPORT", "ROBINSON MUNICIPAL AIRPORT",
            "GILLESPIE CO", "QUAKERTOWN AIRPORT", "UPSHUR COUNTY RGNL AIRPORT",
            "MOUNT CARMEL MUNICIPAL AIRPORT",
            "FRANKFORT DOW MEMORIAL FIELD AIRPORT", "WATONGA AIRPORT",
            "WAUPACA MUNICIPAL AIRPORT", "CHEROKEE MUNICIPAL AIRPORT/",
            "RALPH WENZ FIELD AIRPORT", "ALLEN PARISH AIRPORT",
            "GREENE COUNTY REGIONAL AIRPORT", "BALDWIN COUNTY AIRPORT",
            "OSKALOOSA MUNICIPAL AIRPORT",
            "ALTUS/QUARTZ MOUNTAIN REGIONAL AIRPORT",
            "CLINTON REGIONAL AIRPORT", "CUSHING MUNICIPAL AIRPORT",
            "EL RENO REGIONAL AIRPORT", "SLAYTON MUNICIPAL AIRPORT",
            "HREE RIVERS MUNICIPAL DR HAINES AIRPORT",
            "PLANT CITY MUNICIPAL AIRPORT", "PETER O KNIGHT AIRPORT",
            "DRUMMOND ISLAND AIRPORT",
            "THE ALBERTVILLE MUNI ARPT-THOMAS J BRUMLIK FLD",
            "WAYNE COUNTY AIRPORT", "JACK EDWARDS AIRPORT",
            "HOMESTEAD AFB AIRPORT", "FOLSOM FIELD AP",
            "WASECA MUNICIPAL AIRPORT", "SOUTH LAFOURCHE AIRPORT",
            "WOOD COUNTY AIRPORT MINEOLA", "ADA MUNICIPAL AIRPORT",
            "ORLANDO INTERNATIONAL AIRPORT",
            "OCALA INTERNATIONAL AIRPORT-JIM TAYLOR FIELD",
            "DOUGLAS MUNICIPAL AIRPORT", "CHICKASHA MUNICIPAL ARPT",
            "CARMI MINICIPAL AIRPORT", "VERMILION COUNTY AIRPORT",
            "HALLIBURTON FIELD AIRPORT", "DAVIDSON COUNTY AIRPORT",
            "GALESBURG MUNICIPAL ARPT", "CLAREMORE REGIONAL AIRPORT",
            "GROVE MUNICIPAL AIRPORT", "GRAND PRAIRIE MUNICIPAL AIRPORT",
            "HENDERSON EXECUTIVE ARPT", "EAST HAMPTON AIRPORT",
            "FOX STEPHENS FIELD - GILMER MINICIPAL AIRPORT",
            "GIDDINGS-LEE COUNTY AIRPORT", "BUFFALO MUNICIPAL AIRPORT",
            "CROSS CITY AIRPORT", "BARTOW MUNICIPAL AIRPORT",
            "LICONTN-LINCOLN CO RGNL AP", "BRUNSWICK GOLDEN ISLES APT",
            "LANCASTER AIRPORT", "MOULTRIE MUNICIPAL AIRPORT",
            "WEST WOODWARD AIRPORT", "DALTON MUNICIPAL AIRPORT",
            "ANNAPOLIS UNITED STATES NAVAL ACADEMY", "MID VALLEY AIRPORT",
            "OKMULGEE MUNICIPAL AIRPORT", "OLIVE BRANCH AIRPORT",
            "EDGAR COUNTY AIRPORT", "PAULS VALLEY MUNI AIRPORT",
            "HALE COUNTY AIRPORT", "ROBINS AFB AIRPORT",
            "ANDREWS-MURPHY AIRPORT", "ROBERT S KERR AIRPORT",
            "SHAWNEE MUNICIPAL AIRPORT", "SEARCY MUNICIPAL AIRPORT",
            "AVENGER FIELD AIRPORT", "EGLIN AFB AIRPORT", "NORTH AF AUX",
            "WAYNE MUNICIPAL AIRPORT", "MYERS FIELD AIRPORT",
            "MOREHOUSE MEMORIAL AIRPORT",
            "MARSHFIELD MUNICIPAL AIRPORT - GEORGE HARLOW FIELD",
            "MAXWELL AFB AIRPORT", "DOBBINS AIR RESERVE BASE AIRPORT",
            "NATCHITOCHES REGIONAL ARPT", "HARRY P WILLIAMS MEMO ARPT",
            "TOMAHAWK REGIONAL AIRPORT", "BOOTHVILLE",
            "JIM HOGG COUNTY AIRPORT", "TRACY MUNICIPAL AIRPORT",
            "SOUTH HAVEN AREA REGIONAL AIRPORT", "OWOSSO COMMUNITY AIRPORT",
            "WHARTON REGIONAL AIRPORT", "SULPHUR SPRINGS MUNICIPAL AIRPORT",
            "EDWARDS COUNTY AIRPORT", "SALT POINT", "ELLINGTON FIELD AIRPORT",
            "BARKSDALE AIR FORCE BASE",
            "LACKLAND AIR FORCE BASE (KELLY FIELD ANNEX)",
            "RANDOLPH AFB AIRPORT", "KRVL MUNI/LUIS SHRER FD AP",
            "GAINESVILLE MUNICIPAL ARPT", "TSTC WACO",
            "MC GREGOR EXECUTIVE ARPT", "COX FIELD AIRPORT",
            "HEMPHILL COUNTY AIRPORT", "MARFA MUNICIPAL AIRPORT",
            "BROWNWOOD REGIONAL AIRPORT", "SIERRA BLANCA RGNL AIRPORT",
            "ALAMOGORDO-WHITE SANDS RGL AIRPORT", "BIGGS AAF",
            "GRANT COUNTY AIRPORT", "DAVIS-MONTHAN AFB AIRPORT",
            "LUKE AFB AIRPORT", "MARCH AIR RESERVE BASE",
            "SAN BERNARDINO INTL", "SAN NICOLAS ISLAND NAVAL OUTLYING FIELD",
            "NALF/F. SHERMAN FLD ARPT", "LITCHFIELD MUNICIPAL AIRPORT",
            "POPE AFB AIRPORT", "MACKALL AAF AIRPORT",
            "DARE COUNTY REGIONAL AIRPORT", "STATESVILLE MUNICIPAL ARPT",
            "USMC BOMB RANGE BT-11", "PITT-GREENVILLE AIRPORT",
            "SEYMOUR-JOHNSON AFB AIRPORT",
            "KINSTON REGIONAL JETPORT AT STALLING FIELD",
            "ALBERT J ELLIS AIRPORT", "TRI-COUNTY AIRPORT",
            "FRANKLIN MUNICIPAL-JOHN BEVERLY ROSE AIRPORT",
            "FELKER ARMY AIRFIELD", "DONALDSON CENTER AIRPORT",
            "Kings Land O' Lakes Airport", "SPARTANBURG DOWNTOWN MEM",
            "RURFTON CO-MARCHMAN FLD AP", "ASHE COUNTY AIRPORT",
            "MORGANTON-LENOIR AIRPORT", "ROWAN COUNTY AIRPORT",
            "MOUNT AIRY/SURRY CO ARPT", "ARKANSAS INTERNATIONAL AIRPORT",
            "ALBION MUNICIPAL AIRPORT", "ROGERS MUNI-CARTER FLD APT",
            "ALTUS AFB AIRPORT", "TINKER AFB AIRPORT",
            "HENRY POST AAF AIRPORT", "GRANTS-MILAN MUNI AIRPORT",
            "ORANGE COUNTY AIRPORT", "LOS ALAMOS AIRPORT",
            "RUSK COUNTY AIRPORT", "MC CURTAIN COUNTY REGIONAL AIRPORT",
            "LAUGHLIN/BULLHEAD INTERNATIONAL AIRPORT",
            "EDWARDS AIR FORCE BASE", "BARSTOW-DAGGETT AIRPORT",
            "SOUTHERN CALIFORNIA LOGISTICS AIRPORT",
            "PORTERVILLE MUNICIPAL ARPT", "VANDENBERG AFB",
            "DAVISON AAF AIRPORT", "MOUNTIAN EMPIRE AIRPORT",
            "PHILLIPS ARMY AIRFIELD", "VIRGINIA HIGHLANDS AIRPORT", "TIPTON",
            "AEROFLEX-ANDOVER AIRPORT", "MONMOUTH EXECUTIVE AIRPORT",
            "DOVER AFB AIRPORT", "NAES/MAXFIELD FIELD", "MCGUIRE AFB AIRPORT",
            "SHENANDOAH VALLEY RGNL ART", "TWIN COUNTY AIRPORT",
            "VIRGINIA TECH AIRPORT", "GREENBRIER VALLEY ARIPORT",
            "HENDERSON CITY-COUNTY ARPT", "RICKENBACKER INTL AIRPORT",
            "SCOTT AIR FORCE BASE/MIDAMERICA AIRPORT",
            "SOMERSET-PULASKI CO-J.T. WILSON FIELD AIRPORT",
            "COLUMBUS MUNICIPAL AIRPORT", "HUNTINGBURG AIRPORT",
            "KOKOMO MUNICIPAL AIRPORT", "FARMINGTON REGIONAL ARPT",
            "AGRICULTURAL SCIENCE CENTER", "WHITEMAN AFB AIRPORT",
            "NEWTON-CITY-COUNTY AIRPORT", "MARSHALL ARMY AIRFIELD",
            "GUNSN-CRSTED BUTTE RGL APT", "BUTTS AAF AIRPORT",
            "BUCKLEY AIR FORCE BASE", "SACRAMENTO MCCLELLAN AFB",
            "BEALE AIR FORCE BASE",
            "REID-HILLVIEW AIRPORT OF SANTA CLARA COUNTY",
            "CAIRO REGIONAL AIRPORT", "MONTAUK AIRPORT",
            "NORTH CENTRAL STATE ARPT", "BLOCK ISLAND STATE AIRPORT",
            "MUIR ARMY AIRFIELD (FORT INDIANTOWN GAP)",
            "ITHACA TOMPKINS REGIONAL AIRPORT", "RUTLAND STATE AIRPORT",
            "INDIANA COUNTY/JIMMY STEWART FIELD/AIRPORT",
            "GRINNELL REGIONAL AIRPORT", "GRISSOM AFB AIRPORT",
            "JOLIET REGIONAL AIRPORT", "GROSSE ILE MUNICIPAL AIRPORT",
            "SELFRIDGE AIR NATIONAL GUARD BASE", "KIRSCH MUNICIPAL AIRPORT",
            "COPPER HARBOR", "GRATIOT COMMUNITY AIRPORT",
            "HURON COUNTY MEMORIAL AIRPORT", "BROOKS FIELD AIRPORT",
            "ROBEN-HOOD ARPT", "MASON JEWETT FIELD AIRPORT", "CUSTER AIRPORT",
            "ATLANTIC MUNICIPAL AIRPORT", "CHARLES CITY MUNICIPAL APT",
            "CLINTON MUNICIPAL AIRPORT", "AUDUBON COUNTY AIRPORT",
            "YORK MUNICIPAL AIRPORT", "BEATRICE MUNICIPAL AIRPORT",
            "AINSWORTH MUNICIPAL ARPT", "SEARLE FIELD AIRPORT",
            "JIM KELLY FIELD AIRPORT", "HILL AFB AIRPORT", "WENDOVER AIRPORT",
            "BROOKINGS", "HANCOCK CO-BAR HARBOR ARPT",
            "KNOX COUNTY REGIONAL ARPT", "MT. WASHINGTON OBSERVATORY",
            "LACONIA MUNICIPAL AIRPORT", "DILLANT-HOPKINS AIRPORT",
            "AUBURN/LEWISTON MUNI ARPT", "MAINE FOREST SERVICE",
            "WEXFORD COUNTY AIRPORT", "OSCODA-WURTSMITH AIRPORT",
            "TAYLOR COUNTY AIRPORT", "L.O. SIMENSTAD MUNICIPAL AIRPORT",
            "RICHARD I BONG AIRPORT", "VOLK FIELD AIRPORT",
            "SPARTA/FORT MC COY AIRPORT", "WATERTOWN MUNICIPAL AIRPORT",
            "CENTRAL WISCONSIN AIRPORT", "APPLETON MUNICIPAL AIRPORT",
            "RICE LAKE REGIONAL-CARL'S FIELD AIRPORT", "PRICE COUNTY AIRPORT",
            "MEONE-MARINETTE TWIN CO AP", "IOWA COUNTY AIRPORT",
            "CHAMBERLAIN MUNI AIRPORT", "FAITH MUNICIPAL AIRPORT",
            "COOK MUNICIPAL AIRPORT", "ST JAMES MUNICIPAL AIRPORT",
            "SW MN RGNL MRSHL/RYAN FIELD AIRPORT", "WADENA MUNICIPAL AIRPORT",
            "FARIBAULT MUNICIPAL ARPT",
            "FERGUS FALLS MUNICIPAL AIRPORT-EINAR MICKELSON FLD",
            "MANKATO MUNICIPAL AIRPORT", "FAIRMONT MUNICIPAL AIRPORT",
            "WORTHINGTON MUNICIPAL ARPT", "ALBERT LEA MUNICIPAL ARPT",
            "ELLSWORTH AIR FORCE BASE", "BUFFALO", "DAWSON COMMUNITY AIRPORT",
            "YELLOWSTONE AIRPORT", "CALDWELL INDUSTRIAL ARPT",
            "MOUNTAIN HOME AFB AIRPORT", "ROME STATE AIRPORT",
            "NERN MAINE RGNL ARPT AT PRESQUE IS AIRPORT",
            "PRESQUE ISLE COUNTY AIRPORT",
            "MARQUETTE MICHIGAN COUNTY AP (WFO)", "MACKINAC  ISLAND AIRPORT",
            "GOGEBIC-IRON COUNTY ARPT", "DETRT LKS-WETHING FLD ARPT",
            "GRAND RAPIDS/ITASCA CO-G NEWSTROM FIELD ARPT",
            "ELY MUNICIPAL AIRPORT", "SCOTTS SPB",
            "ATKN MUNI-S KURTZ FLD ARPT", "BENSON MUNICIPAL AIRPORT",
            "PINE RIVER REGIONAL AIRPORT", "BEMIDJI-BELTRAMI CO ARPT",
            "THIEF RIVER FALLS RGNL APT", "DEVILS LAKE MUNI AIRPORT",
            "GRAND FORKS AFB AIRPORT", "MINOT AFB AIRPORT", "GARRISON",
            "JORDAN AIRPORT", "SIDNEY-RICHLAND MUNI ARPT", "GREAT FALLS",
            "COEUR D'ALENE AIR TERM APT", "FAIRCHILD AIR FORCE BASE",
            "KELSO-LONGVIEW AIRPORT", "MICHAEL AAF AIRPORT",
            "MCCHORD AFB AIRPORT", "PLYMOUTH MUNICIPAL AIRPORT",
            "MASON COUNTY AIRPORT", "HARRISBURG-RALEIGH AIRPORT",
            "SPARTA COMMUNITY-HUNTER FIELD AIRPORT",
            "FAIRFIELD MUNICIPAL ARPT", "CENTRALIA MUNICIPAL ARPT",
            "FLORA MUNICIPAL AIRPORT", "OLNEY-NOBLE AIRPORT",
            "TAYLORVILLE MINICIPAL ARPT", "EAST MILTON",
            "WESTOVER AFB/METROPOLITAN AIRPORT", "LANGLEY AFB AIRPORT",
            "BLUE RIDGE AIRPORT", "MELROSE GUNNERY RANGE  NM.",
            "CAMPBELL AAF AIRPORT", "SIMMONS AAF AIRPORT",
            "HOLLOMAN AFB AIRPORT", "COMANCHE COUNTY-CITY AIRPORT",
            "KEESLER AIR FORCE BASE", "TYNDALL AFB AIRPORT",
            "HUNTER ARMY AIRFIELD", "STATESBORO-BULLOCK CO ARPT",
            "THOMASTON-UPSON CO AIRPORT", "MAC DILL AFB AIRPORT",
            "SHAW AIR FORCE BASE", "KENNEDY SPACE CENTER",
            "PATRICK AFB AIRPORT", "RAFAEL HERNANDEZ AIRPORT"
        ],
        'latitude': [
            -15.883, 34.3, 66.6, 65.983, 70.331, 68.479, 54.85, 70.134, 68.867,
            68.35, 66, 66.817, 68.115, 64.55, 63.687, 63.767, 63.883, 62.785,
            61.783, 60.383, 61.524, 64.935, 62.894, 61.582, 61.572, 61.1,
            63.886, 60.476, 58.096, 57.58, 64.727, 63.733, 64.683, 70.467,
            61.949, 61.253, 61.416, 61.132, 60.541, 55.17, 59.324, 56.959,
            56.311, 58.185, 61.717, 59.433, 65.698, 56.967, 55.206, 56.933,
            55.131, 43.733, 30.784, 42.543, 37.186, 34.545, 46.417, 31.397,
            32.915, 38.955, 30.983, 27.207, 48.467, 28.973, 34.273, 26.442,
            35.256, 32.444, 33.714, 33.53, 33.78, 32.084, 30.886, 31.869,
            32.456, 32.646, 30.872, 40.1, 33.254, 34.861, 33.096, 31.78,
            27.779, 33.11, 39.016, 30.243, 40.435, 39, 38.607, 44.626, 35.864,
            44.333, 42.732, 42.796, 30.75, 33.598, 33.154, 41.226, 34.699,
            35.538, 35.95, 35.473, 43.987, 41.96, 28, 27.916, 46.007, 34.229,
            36.855, 30.291, 25.483, 34.269, 44.074, 29.445, 32.742, 34.804,
            28.434, 29.167, 31.477, 35.096, 38.089, 40.2, 34.471, 35.781,
            40.933, 36.294, 36.605, 32.699, 35.976, 40.96, 32.699, 30.169,
            45.159, 29.633, 27.95, 35.483, 31.259, 32.579, 31.083, 36.437,
            34.722, 38.99, 26.178, 35.668, 34.979, 39.7, 34.711, 34.167,
            32.633, 35.195, 35.021, 35.357, 35.212, 32.473, 30.483, 33.615,
            42.242, 44.729, 32.756, 42.098, 32.383, 33.917, 31.736, 29.717,
            45.469, 29.33, 27.349, 44.249, 42.351, 42.993, 29.266, 33.167,
            29.947, 29.562, 29.617, 32.5, 29.383, 29.533, 29.983, 33.651,
            31.638, 31.485, 33.633, 35.9, 30.371, 31.8, 33.45, 32.84, 31.85,
            32.633, 32.167, 33.55, 33.9, 34.095, 33.24, 33.023, 39.163, 35.174,
            35.033, 35.917, 35.765, 35.017, 35.633, 35.344, 35.317, 34.833,
            36.298, 36.698, 37.133, 34.758, 46.15, 34.916, 35.428, 36.432,
            35.821, 35.646, 36.46, 35.967, 41.73, 36.372, 34.65, 35.417, 34.65,
            35.165, 30.069, 35.883, 45.497, 33.909, 35.157, 34.9, 34.854,
            34.583, 36.029, 34.717, 38.717, 36.895, 39.472, 36.683, 39.085,
            41.009, 40.183, 39.133, 40.033, 40.017, 38.264, 36.766, 37.208,
            37.867, 37.8, 39.817, 38.55, 37.054, 39.267, 38.249, 40.528,
            37.761, 39.823, 38.717, 38.068, 39.05, 38.533, 38.678, 39.717,
            38.667, 39.133, 37.333, 37.064, 41.073, 41.921, 41.168, 40.433,
            42.483, 43.533, 40.633, 41.717, 40.65, 41.5, 42.099, 42.608,
            41.817, 47.467, 43.322, 43.78, 42.251, 43.717, 42.566, 41.94,
            41.407, 43.073, 41.833, 41.7, 40.894, 40.301, 42.577, 41.119,
            40.789, 41.117, 40.721, 42.074, 44.45, 44.067, 44.267, 43.567,
            42.9, 44.05, 45.462, 44.283, 44.45, 45.101, 45.308, 46.689, 43.933,
            43.967, 43.167, 44.783, 45.228, 45.419, 45.709, 45.117, 42.887,
            43.767, 45.032, 47.822, 43.986, 44.45, 46.447, 44.333, 46.283,
            44.217, 43.65, 43.645, 43.683, 44.15, 45.604, 47.133, 44.683,
            43.65, 43.05, 42.591, 46.683, 45.407, 46.531, 45.865, 46.533,
            46.833, 47.211, 47.817, 48.267, 46.548, 45.332, 46.725, 47.5,
            48.067, 48.117, 47.967, 48.417, 47.646, 47.326, 47.717, 47.45,
            47.767, 47.633, 46.117, 40.183, 47.15, 43.779, 38.915, 37.811,
            38.149, 38.379, 38.515, 38.665, 38.722, 39.534, 42.212, 42.2,
            37.083, 36.631, 34.3, 36.667, 35.133, 32.85, 31.917, 30.417,
            30.067, 32.017, 32.483, 32.955, 27.85, 33.967, 28.617, 28.233,
            18.498
        ],
        'longitude': [
            54.517, -116.167, -159.986, -161.133, -149.598, -149.49, -163.417,
            -143.577, -166.133, -166.8, -153.7, -150.65, -145.579, -163.007,
            -170.493, -171.733, -160.8, -164.491, -166.033, -166.2, -166.147,
            -161.155, -155.976, -159.543, -149.541, -155.583, -152.302,
            -151.034, -135.409, -157.58, -155.47, -148.917, -147.083, -157.436,
            -147.169, -149.794, -149.507, -146.244, -165.087, -162.27,
            -155.902, -158.632, -158.373, -157.386, -157.15, -146.333,
            -156.351, -133.9, -132.828, -154.183, -131.578, -96.633, -98.662,
            -83.178, -88.751, -94.203, -86.65, -84.895, -85.963, -121.082,
            -84.633, -98.121, -122.417, -95.863, -78.715, -98.129, -81.601,
            -97.817, -96.674, -82.516, -82.816, -97.097, -94.035, -95.218,
            -96.913, -81.596, -96.622, -75.267, -97.581, -86.557, -94.961,
            -95.706, -97.691, -98.555, -87.65, -98.91, -75.382, -80.274,
            -87.727, -86.201, -98.421, -89.02, -95.556, -109.807, -92.688,
            -83.139, -83.241, -92.491, -99.338, -98.933, -96.773, -98.006,
            -95.783, -85.593, -82.164, -82.449, -83.743, -86.256, -84.856,
            -87.672, -80.383, -86.858, -93.553, -90.261, -95.496, -96.671,
            -81.325, -82.233, -82.861, -97.966, -88.123, -87.6, -97.951,
            -80.304, -90.433, -95.479, -94.738, -97.047, -115.133, -72.252,
            -94.949, -96.98, -93.843, -83.105, -81.783, -81.161, -81.466,
            -96.719, -83.8, -99.521, -84.869, -76.48, -97.973, -95.949,
            -89.787, -87.669, -97.223, -101.717, -83.6, -83.865, -94.621,
            -96.943, -91.737, -100.466, -86.517, -81.084, -96.983, -96.266,
            -91.881, -70.672, -86.35, -84.517, -93.099, -91.333, -89.806,
            -89.4, -98.737, -95.607, -86.256, -84.139, -96.008, -95.617,
            -100.173, -91.526, -95.167, -93.667, -98.583, -98.262, -99.083,
            -97.197, -97.074, -97.316, -95.45, -100.4, -104.017, -98.95,
            -105.517, -105.991, -106.38, -108.167, -110.883, -112.367, -117.25,
            -117.235, -119.458, -118.588, -89.675, -79.009, -79.5, -75.7,
            -80.957, -76.467, -77.383, -77.965, -77.633, -77.617, -77.171,
            -76.903, -76.6, -82.376, -89.217, -81.957, -81.935, -81.419,
            -81.611, -80.52, -80.553, -89.95, -98.054, -94.107, -99.267,
            -97.383, -98.4, -107.902, -93.804, -106.283, -91.001, -94.859,
            -114.559, -117.867, -116.786, -117.383, -119.063, -120.567,
            -77.183, -81.35, -76.17, -82.033, -76.759, -74.737, -74.133,
            -75.467, -74.35, -74.6, -78.896, -80.823, -80.408, -80.4, -87.683,
            -82.933, -89.85, -84.615, -85.9, -86.954, -86.059, -90.428,
            -93.579, -93.55, -97.275, -96.767, -106.933, -104.757, -104.75,
            -121.4, -121.433, -121.817, -89.219, -71.923, -71.491, -71.578,
            -76.567, -76.467, -72.95, -79.1, -92.7, -86.15, -88.167, -83.161,
            -82.818, -85.433, -87.883, -84.688, -82.986, -84.956, -85.5,
            -84.433, -83.435, -95.047, -92.611, -90.333, -94.917, -97.626,
            -96.754, -100.001, -101.768, -99.771, -111.967, -114.036, -124.29,
            -68.367, -69.1, -71.3, -71.433, -72.267, -70.283, -69.595, -85.417,
            -83.4, -90.303, -92.69, -92.094, -90.267, -90.733, -88.717,
            -89.667, -96.007, -91.773, -90.402, -87.633, -90.236, -99.318,
            -102.019, -92.689, -94.558, -95.817, -95.212, -93.317, -96.15,
            -93.917, -94.417, -95.58, -93.367, -103.1, -103.546, -104.8,
            -111.117, -116.633, -115.867, -117.864, -68.05, -83.813, -87.549,
            -84.637, -90.133, -95.883, -93.51, -91.833, -92.483, -93.677,
            -95.651, -94.382, -94.933, -96.183, -98.9, -97.4, -101.35,
            -101.439, -106.948, -104.183, -111.383, -116.817, -117.65,
            -122.894, -112.933, -122.483, -71.754, -82.099, -88.549, -89.699,
            -88.413, -89.092, -88.453, -88.176, -89.328, -71.114, -72.533,
            -76.36, -80.018, -103.8, -87.483, -78.933, -106.1, -98.6, -88.917,
            -85.583, -81.133, -81.737, -84.264, -82.517, -80.467, -80.683,
            -80.6, -67.129
        ]
    }

    df_us_weather_station = pd.DataFrame(d_us_weather_station)

    # # Sample benchmarking statistics (for demonstration purposes only)
    ## Electricity
    # From simulation
    d_sample_benchmark_stats_e = {
        # Order: "baseload", "cooling sensitivity", "cooling change-point", "heating sensitivity", "heating change-point"
        'beta_median': [0.352, 0.008635, 11.8, 0.00609, 13.3],
        'beta_standard_deviation': [0.042105175, 0.003189988, 5.128711432, 0.00546208, 5.159961489],
    }
    ## Fossil fuel
    # From simulation
    d_sample_benchmark_stats_f = {
        # Order: "baseload", "cooling sensitivity", "cooling change-point", "heating sensitivity", "heating change-point"
        'beta_median': [0.005805, 0, 0, 0.00698, 13.5],
        'beta_standard_deviation': [0.008327917, 0, 0, 0.00901039, 5.965051821],
    }

    df_sample_benchmark_stats_e = pd.DataFrame(
        data=d_sample_benchmark_stats_e,
        index=["beta_base", "beta_cdd", "beta_betc", "beta_hdd", "beta_beth"])
    df_sample_benchmark_stats_f = pd.DataFrame(
        data=d_sample_benchmark_stats_f,
        index=["beta_base", "beta_cdd", "beta_betc", "beta_hdd", "beta_beth"])

    df_sample_benchmark_stats_e.index.name = "coefficient"
    df_sample_benchmark_stats_f.index.name = "coefficient"

    def read_bench_stats(self, file_name, utility_type):
        # utility_type: 1 ~ electricity, 2 ~ fossil fuel
        df_bench_stats = pd.read_csv(file_name)
        if (utility_type == 1):
            df_sample_benchmark_stats_e = df_bench_stats
            df_sample_benchmark_stats_e.index.name = "coefficient"
        else:
            df_sample_benchmark_stats_f = df_bench_stats
            df_sample_benchmark_stats_f.index.name = "coefficient"

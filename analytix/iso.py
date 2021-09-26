# Copyright (c) 2021, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

COUNTRIES = (
    "AW",
    "AF",
    "AO",
    "AI",
    "AX",
    "AL",
    "AD",
    "AE",
    "AR",
    "AM",
    "AS",
    "AQ",
    "TF",
    "AG",
    "AU",
    "AT",
    "AZ",
    "BI",
    "BE",
    "BJ",
    "BQ",
    "BF",
    "BD",
    "BG",
    "BH",
    "BS",
    "BA",
    "BL",
    "BY",
    "BZ",
    "BM",
    "BO",
    "BR",
    "BB",
    "BN",
    "BT",
    "BV",
    "BW",
    "CF",
    "CA",
    "CC",
    "CH",
    "CL",
    "CN",
    "CI",
    "CM",
    "CD",
    "CG",
    "CK",
    "CO",
    "KM",
    "CV",
    "CR",
    "CU",
    "CW",
    "CX",
    "KY",
    "CY",
    "CZ",
    "DE",
    "DJ",
    "DM",
    "DK",
    "DO",
    "DZ",
    "EC",
    "EG",
    "ER",
    "EH",
    "ES",
    "EE",
    "ET",
    "FI",
    "FJ",
    "FK",
    "FR",
    "FO",
    "FM",
    "GA",
    "GB",
    "GE",
    "GG",
    "GH",
    "GI",
    "GN",
    "GP",
    "GM",
    "GW",
    "GQ",
    "GR",
    "GD",
    "GL",
    "GT",
    "GF",
    "GU",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IM",
    "IN",
    "IO",
    "IE",
    "IR",
    "IQ",
    "IS",
    "IL",
    "IT",
    "JM",
    "JE",
    "JO",
    "JP",
    "KZ",
    "KE",
    "KG",
    "KH",
    "KI",
    "KN",
    "KR",
    "KW",
    "LA",
    "LB",
    "LR",
    "LY",
    "LC",
    "LI",
    "LK",
    "LS",
    "LT",
    "LU",
    "LV",
    "MO",
    "MF",
    "MA",
    "MC",
    "MD",
    "MG",
    "MV",
    "MX",
    "MH",
    "MK",
    "ML",
    "MT",
    "MM",
    "ME",
    "MN",
    "MP",
    "MZ",
    "MR",
    "MS",
    "MQ",
    "MU",
    "MW",
    "MY",
    "YT",
    "NA",
    "NC",
    "NE",
    "NF",
    "NG",
    "NI",
    "NU",
    "NL",
    "NO",
    "NP",
    "NR",
    "NZ",
    "OM",
    "PK",
    "PA",
    "PN",
    "PE",
    "PH",
    "PW",
    "PG",
    "PL",
    "PR",
    "KP",
    "PT",
    "PY",
    "PS",
    "PF",
    "QA",
    "RE",
    "RO",
    "RU",
    "RW",
    "SA",
    "SD",
    "SN",
    "SG",
    "GS",
    "SH",
    "SJ",
    "SB",
    "SL",
    "SV",
    "SM",
    "SO",
    "PM",
    "RS",
    "SS",
    "ST",
    "SR",
    "SK",
    "SI",
    "SE",
    "SZ",
    "SX",
    "SC",
    "SY",
    "TC",
    "TD",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TM",
    "TL",
    "TO",
    "TT",
    "TN",
    "TR",
    "TV",
    "TW",
    "TZ",
    "UG",
    "UA",
    "UM",
    "UY",
    "US",
    "UZ",
    "VA",
    "VC",
    "VE",
    "VG",
    "VI",
    "VN",
    "VU",
    "WF",
    "WS",
    "YE",
    "ZA",
    "ZM",
    "ZW",
)
SUBDIVISIONS = (
    "US-OH",
    "US-IN",
    "US-OK",
    "US-KS",
    "US-OR",
    "US-KY",
    "US-PA",
    "US-LA",
    "US-AK",
    "US-PR",
    "US-MA",
    "US-AL",
    "US-RI",
    "US-MD",
    "US-AR",
    "US-SC",
    "US-ME",
    "US-AS",
    "US-SD",
    "US-MI",
    "US-AZ",
    "US-TN",
    "US-MN",
    "US-CA",
    "US-TX",
    "US-MO",
    "US-CO",
    "US-UM",
    "US-MP",
    "US-CT",
    "US-UT",
    "US-MS",
    "US-DC",
    "US-VA",
    "US-MT",
    "US-DE",
    "US-VI",
    "US-NC",
    "US-FL",
    "US-VT",
    "US-ND",
    "US-GA",
    "US-WA",
    "US-NE",
    "US-GU",
    "US-WI",
    "US-NH",
    "US-HI",
    "US-WV",
    "US-NJ",
    "US-IA",
    "US-WY",
    "US-NM",
    "US-ID",
    "US-NV",
    "US-IL",
    "US-NY",
)
CURRENCIES = (
    "AED",
    "AFN",
    "ALL",
    "AMD",
    "ANG",
    "AOA",
    "ARS",
    "AUD",
    "AWG",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BGN",
    "BHD",
    "BIF",
    "BMD",
    "BND",
    "BOB",
    "BRL",
    "BSD",
    "BTN",
    "BWP",
    "BYN",
    "BZD",
    "CAD",
    "CDF",
    "CHF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CUC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOP",
    "DZD",
    "EGP",
    "ERN",
    "ETB",
    "EUR",
    "FJD",
    "FKP",
    "GBP",
    "GEL",
    "GHS",
    "GIP",
    "GMD",
    "GNF",
    "GTQ",
    "GYD",
    "HKD",
    "HNL",
    "HRK",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KMF",
    "KPW",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LRD",
    "LSL",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRO",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SBD",
    "SCR",
    "SDG",
    "SEK",
    "SGD",
    "SHP",
    "SLL",
    "SOS",
    "SRD",
    "SSP",
    "STD",
    "SVC",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TOP",
    "TRY",
    "TTD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "USD",
    "UYU",
    "UZS",
    "VEF",
    "VND",
    "VUV",
    "WST",
    "XAF",
    "XAG",
    "XAU",
    "XBA",
    "XBB",
    "XBC",
    "XBD",
    "XCD",
    "XDR",
    "XOF",
    "XPD",
    "XPF",
    "XPT",
    "XSU",
    "XTS",
    "XUA",
    "XXX",
    "YER",
    "ZAR",
    "ZMW",
    "ZWL",
)

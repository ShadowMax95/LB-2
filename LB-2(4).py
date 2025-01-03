from bottle import route, run, request
@route('/type')
def get_type():
    xml_file = """ <exchange>
                        <currency>
                            <exchangedate>04.12.2024</exchangedate>
                            <r030>840</r030>
                            <cc>USD</cc>
                            <txt>Долар США</txt>
                            <enname>US Dollar</enname>
                            <rate>41.6972</rate>
                            <units>1</units>
                            <rate_per_unit>41.6972</rate_per_unit>
                            <group>1</group>
                            <calcdate>03.12.2024</calcdate>
                        </currency>
                    </exchange>"""

    json_file = """[
            {
                "exchangedate": "04.12.2024",
                "r030": 840,
                "cc": "USD",
                "txt": "Долар США",
                "enname": "US Dollar",
                "rate": 41.6972,
                "units": 1,
                "rate_per_unit": 41.6972,
                "group": "1",
                "calcdate": "03.12.2024"
            }
        ]"""

    if request.get_header('Content-Type') == "application/xml":
        return xml_file
    elif request.get_header('Content-Type') == "application/json":
        return json_file
    else:
        return "04.12.2024 USD exchange rate is 41.6972"


if __name__ == '__main__':
    run(host='localhost', port=8000)

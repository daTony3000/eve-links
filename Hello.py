# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="EvE Links by Tony",
        page_icon="👋",
    )
  
    # st.header("EvE Links")

    st.markdown(
        """
       ##### Wurmloch
        - [Pathfinder](https://pathfinder.lost-in-w.space) &nbsp;&nbsp;&rarr;&nbsp;&nbsp; Wormhole Mapper
        - [EvE-Scout](https://www.eve-scout.com/thera) &nbsp;&nbsp;&rarr;&nbsp;&nbsp; Thera-Verbindungen
        - [Anoikis](http://anoik.is) &nbsp;&nbsp;&rarr;&nbsp;&nbsp; Wurmlochsysteme
      ##### Markt
        - [GoonPraisal](https://appraise.imperium.nexus) &nbsp;&nbsp;&rarr;&nbsp;&nbsp; An- und Verkaufspreise
        - [EvE Tycoon](https://evetycoon.com/market) &nbsp;&nbsp;&rarr;&nbsp;&nbsp; Markt-Browser
      ##### Sonstiges
        - [Dotlan](https://evemaps.dotlan.net/map) &nbsp;&nbsp;&rarr;&nbsp;&nbsp; 2D-Map
        - [zKill](https://zkillboard.com/) &nbsp;&nbsp;&rarr;&nbsp;&nbsp; Killboard



    """
    )


if __name__ == "__main__":
    run()

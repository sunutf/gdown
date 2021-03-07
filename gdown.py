import matplotlib
#matplotlib.use('inline')

import requests
import re
import os
import os.path as pth
import tarfile

from multiprocessing import Pool
from functools import partial


import zipfile

minik_txt_url_list = [
	'https://drive.google.com/file/d/1V4YdEugaMVfrhpgP9eiZ4GjNTlNTK87M/view?usp=sharing',
	'https://drive.google.com/file/d/1etaGqlDrwR0R-l5wpMLaQy-K8sWaFK9I/view?usp=sharing',
	'https://drive.google.com/file/d/1UYEOjHzhAy8DYmfwIeoVzZTtLr7DDgUS/view?usp=sharing'
]
fcvid_url_list = [
    'https://drive.google.com/file/d/1aCdS0PExl1lGrBwEWFb1nHbacQZzlJm6/view?usp=sharing',
    'https://drive.google.com/file/d/15IuSzvl0223nCRbZfDCi7vvXkN2q817L/view?usp=sharing',
    'https://drive.google.com/file/d/1cUhKww6onqGO8eMHiKEHg9fp2EqL633C/view?usp=sharing',
    'https://drive.google.com/file/d/1rLndgx6Klpzb2-NUV9NCbRg14w6IjtUN/view?usp=sharing',
    'https://drive.google.com/file/d/1Wo__tjDZMbsaY74jrChqqeQkUb5BmbIg/view?usp=sharing',
    'https://drive.google.com/file/d/1YsHANcit_LfW1xLdJVwidKdVhplSzbEk/view?usp=sharing',
    'https://drive.google.com/file/d/19n6EBDKzTCzShVduiWCO2DHhXRo7WRAL/view?usp=sharing',
    'https://drive.google.com/file/d/1T6vSwc0C-nR-BAHAmtUBWnblHTcZwuHl/view?usp=sharing',
    'https://drive.google.com/file/d/1VaaXVw95I6lmVYPSVST7xv38D82d4AsW/view?usp=sharing',
    'https://drive.google.com/file/d/1zAZTY9SO5a1OO2sV1pP2WSc3aQ5jmmWw/view?usp=sharing',
    'https://drive.google.com/file/d/1A3iWXlPCWLupO6a8kMzi-CY38mdOTQZY/view?usp=sharing',
    'https://drive.google.com/file/d/1PoJq3D_dxCrGlR1I_vg7626PhZcltLDH/view?usp=sharing',
    'https://drive.google.com/file/d/12fCtg6tcBcxCm3VPnTmnEvFrH7y5YqZa/view?usp=sharing',
    'https://drive.google.com/file/d/1SStgmBvKaCuWvfN_KUn3Vit5vMzAl5J_/view?usp=sharing',
    'https://drive.google.com/file/d/1I4Pd6j8pLeFrQtWVSfJ8FF1Ozi1st0vq/view?usp=sharing',
    'https://drive.google.com/file/d/1Y7sCu1WcKk1KuVJMihin0LozmFWcSb_G/view?usp=sharing',
    'https://drive.google.com/file/d/1RSq2mlYiYuic1SPOVkrj2IUJklUUmWve/view?usp=sharing',
    'https://drive.google.com/file/d/1b0ZVfCTvkIBYHJOWRKnIK5I14EK42jW6/view?usp=sharing',
    'https://drive.google.com/file/d/12ZbTvjUbQtPkP-4exGly383RVkI2rAcY/view?usp=sharing',
    'https://drive.google.com/file/d/1PIfQJ2p378x9FpJ3sea2oM9psFFToEIr/view?usp=sharing',
    'https://drive.google.com/file/d/1WDWI3om8xqZrnQ-clXP7ndZL6B8Z6xxP/view?usp=sharing',
    'https://drive.google.com/file/d/1WvXPZTf-x9aluzCVGTxduulvtRe7A6my/view?usp=sharing',
    'https://drive.google.com/file/d/1NpzNWetTsvuBoVmshBaV3GFA72n5MMCp/view?usp=sharing',
    'https://drive.google.com/file/d/1prmA5AWOmLIyZyKi1etev8KAE4hS7A4S/view?usp=sharing',
    'https://drive.google.com/file/d/1prmA5AWOmLIyZyKi1etev8KAE4hS7A4S/view?usp=sharing',
    'https://drive.google.com/file/d/13aH-gECxqBRrA7ythVZ9IFk5--IsrNNS/view?usp=sharing',
    'https://drive.google.com/file/d/1A3qMh5Qvcty7x2IELIurrN-_fjYvEeyT/view?usp=sharing',
    'https://drive.google.com/file/d/1foll_J6LzYICMI9sGJwFtyNtRBawZVDE/view?usp=sharing',
    'https://drive.google.com/file/d/1evfPtiVBhhgGv1PdrcGOc1BeXCymz2Y9/view?usp=sharing',
    'https://drive.google.com/file/d/1UrdjbMzrxtJVJ8NYmxa5D_0pB5_zWQ-t/view?usp=sharing',
    'https://drive.google.com/file/d/1vaSOH1ZXzZA3Z6qaFVoEF3RD67PqtyKt/view?usp=sharing',
    'https://drive.google.com/file/d/1veU1IC_IDmkM5KNiGWve-_tIxNqAKy2Y/view?usp=sharing',
    'https://drive.google.com/file/d/1JUS5vKi35Qne6m3sQ1lSEwr64o59oLjh/view?usp=sharing',
    'https://drive.google.com/file/d/1j0i-jTZbh7r2ySMJ8u5IRt9PWGcIBjaN/view?usp=sharing',
    'https://drive.google.com/file/d/1owPM7010eTZHdPsFmTjpQQoaFv-Z6Vkz/view?usp=sharing',
    'https://drive.google.com/file/d/1IKJDP-7LxXETzJ37A7S8WuzzNDcY-ULR/view?usp=sharing',
    'https://drive.google.com/file/d/1It1dfIuugVnob9gjt8gAa5vvD5m_n60v/view?usp=sharing',
    'https://drive.google.com/file/d/1-4AKuQZDp9ynwKZWMaE8zAytT7ASEfJP/view?usp=sharing',
    'https://drive.google.com/file/d/1717xVtB8nWjj5XRBGvJSq8va_lHu1dfT/view?usp=sharing',
    'https://drive.google.com/file/d/1NccYrdgxAvYVRZVtwC1oneI3Jkw48Tlp/view?usp=sharing',
    'https://drive.google.com/file/d/1hYuZqaAorMsGr3bCAlxZUvTmKVHJouoC/view?usp=sharing',
    'https://drive.google.com/file/d/1qLPyIAitalep0pQRuqB2Uj04TgklDlsp/view?usp=sharing',
    'https://drive.google.com/file/d/1rvtPcwlZSVjWuEBYN5szlsqblKiJjgEA/view?usp=sharing',
    'https://drive.google.com/file/d/1gkJMFGkREiS6rjVYdGV-XfiZqNPP08mM/view?usp=sharing',
    'https://drive.google.com/file/d/12tLb9u_DnXlb1PHfJ6oNJ654dOGLzf2I/view?usp=sharing',
    'https://drive.google.com/file/d/18L0zQgRiqW54NTPPyEx843HsBbLI8bFm/view?usp=sharing',
    'https://drive.google.com/file/d/1dIrkRbBMKzklDjQ9Uk5MIlHia6r-W1KW/view?usp=sharing',
    'https://drive.google.com/file/d/1UiFIxd89w2c_ySxfWe6raaB-a162523k/view?usp=sharing',
    'https://drive.google.com/file/d/14vhrLEnUCDBROfZGRuOm603ycm2HqPuQ/view?usp=sharing',
    'https://drive.google.com/file/d/1dgLefIRcyVqLSxeDz8Q4XM_7DTUrIdA-/view?usp=sharing',
    'https://drive.google.com/file/d/1yN2H9M196qOdgRpd68bPfMdFyUu3O_lN/view?usp=sharing',
    'https://drive.google.com/file/d/18tQe3rsxBlB0a1L8Q9L-EIIoKINIBrhL/view?usp=sharing',
    'https://drive.google.com/file/d/1aQ1G0RwYcxR5MJgRe4mZBxblCUVO8MZU/view?usp=sharing',
    'https://drive.google.com/file/d/1aQ1G0RwYcxR5MJgRe4mZBxblCUVO8MZU/view?usp=sharing',
    'https://drive.google.com/file/d/18moEfBVpQzJKFs5iItjwjiInyCfFws9D/view?usp=sharing',
    'https://drive.google.com/file/d/1b5pQbRkQnrH3mML9win30btYGOSuNi_c/view?usp=sharing',
    'https://drive.google.com/file/d/1S8K4cRKQpZgDNzhyb17rY3ckPcSjh3MF/view?usp=sharing',
    'https://drive.google.com/file/d/1ahU42DNyfBkkuqleLKeFTSXRb0I2heo3/view?usp=sharing',
    'https://drive.google.com/file/d/1FHU6Q--oOG2NPUme3InbXF1oiY9NMjFf/view?usp=sharing',
    'https://drive.google.com/file/d/1Bi7QVp5ejR0e_TfIuUSOLsqajAizyJ_D/view?usp=sharing',
    'https://drive.google.com/file/d/1Vaj7SPAH4xAPEz4UPHzZ8fe9jGKSpvcM/view?usp=sharing',
    'https://drive.google.com/file/d/1Yr9tO0wHEXuAiJ54M-FyC4mrVhXECUYc/view?usp=sharing',
    'https://drive.google.com/file/d/1c6igwxMsa6XJzaztBTZMcYauKNFZ6hmu/view?usp=sharing',
    'https://drive.google.com/file/d/1BI0BT2yoiYNKEml_GBf1aX394rXHms9c/view?usp=sharing',
    'https://drive.google.com/file/d/17ldUCyvyRa0i4eTYpwpHu-6D_icyaKEd/view?usp=sharing',
    'https://drive.google.com/file/d/1NwR46jza6m15OMWq8B3LKkjkntTRPgG7/view?usp=sharing',
    'https://drive.google.com/file/d/1sQaKJS9_wmSB-OMMytT9SAwjt-ww7qAL/view?usp=sharing',
    'https://drive.google.com/file/d/1nfRWRzX4NmxsbE3TXM4e-d792fLSE9Kn/view?usp=sharing',
    'https://drive.google.com/file/d/1cELjSvV8GnlFc7L_6avsrIMD2h1DP-px/view?usp=sharing',
    'https://drive.google.com/file/d/1GCbz584ZQL2_gAe3MaIZF4H_MnT18vtH/view?usp=sharing',
    'https://drive.google.com/file/d/1IVk2CZgnG5PIc_COBUXDifhRP44FuUTV/view?usp=sharing',
    'https://drive.google.com/file/d/1rDw5xHkuiiJinqNsLut1QQ7gkhgW3vDq/view?usp=sharing',
    'https://drive.google.com/file/d/1QglUxNm4z3NBo_qronuHXOuSsAja_7it/view?usp=sharing',
    'https://drive.google.com/file/d/1spoDo4-EAjS2xHO2_d5v5TGzMIMRu_od/view?usp=sharing',
    'https://drive.google.com/file/d/1mQ4Oyu-lcHa9M-kU5g5bzKO5mHtvAIMh/view?usp=sharing',
    'https://drive.google.com/file/d/1BskR1dVUbHNrjDvRo5kKQNp6WWHwYe29/view?usp=sharing',
    'https://drive.google.com/file/d/1iRJPeCn2-oDlM4shtKjKD5CRGvVZkRWY/view?usp=sharing',
    'https://drive.google.com/file/d/1ytELfuWeFkJWnUmDiVDTbOKTYE15WqPW/view?usp=sharing',
    'https://drive.google.com/file/d/1UPzE0EmLbISEKT_xPCU8mbWS8J5h5Lz_/view?usp=sharing',
    'https://drive.google.com/file/d/13IvSsLtHUihUHI1zo__6w4zjEyIR5xCW/view?usp=sharing',
    'https://drive.google.com/file/d/1t-BDuQPA9Z7989lhtEgVS9-I3vYxwaRQ/view?usp=sharing',
    'https://drive.google.com/file/d/1SY_P61b2FcOUzfbNBalWqXfu67amxD0K/view?usp=sharing',
    'https://drive.google.com/file/d/10l0q9Fd7Rf9ND6WHTg7fq6J61dJjcqMP/view?usp=sharing',
    'https://drive.google.com/file/d/1NZRWegcWKOCl1-s46rerY6gn9ecsBN8k/view?usp=sharing',
    'https://drive.google.com/file/d/1zGTD6ZlYU73TWM5Yl499No3wC5y9a-CG/view?usp=sharing',
    'https://drive.google.com/file/d/1eqc3cw_uW9GMrEhG2WuuOGX5fwYW8mkt/view?usp=sharing',
    'https://drive.google.com/file/d/1AYTtVLjVA1BBXo3dfO6_o3whM2xuLxd-/view?usp=sharing',
    'https://drive.google.com/file/d/1dnbL2o2q-kyvh2LX0n6bmLBMj2W976c8/view?usp=sharing',
    'https://drive.google.com/file/d/15asztvr9aDWdRD17rdl7E3YCVZfSsEM9/view?usp=sharing',
    'https://drive.google.com/file/d/1RNPLjddCpw6mCrA35WY9woso71VgjDIM/view?usp=sharing',
    'https://drive.google.com/file/d/1Ah1Qj2TyJdrAokIoDFtNrziZUE0dpqpr/view?usp=sharing',
    'https://drive.google.com/file/d/1EcXJHnkSKlk5fgyjAdPmPTkOF0yT26uy/view?usp=sharing',
    'https://drive.google.com/file/d/1mmt087XoEO2eN0xuGPd3-8MwFMEAt6ss/view?usp=sharing',
    'https://drive.google.com/file/d/1alFrZIWsymTh5ekX-NTXnh7ecNh6OD-r/view?usp=sharing',
    'https://drive.google.com/file/d/1ZI6gS2DYugmjS2qFBReiERl6RILlT1HT/view?usp=sharing',
    'https://drive.google.com/file/d/1h1G_IGUQ8qlFlxatSypsE9mkihLDJ0fQ/view?usp=sharing',
    'https://drive.google.com/file/d/1IWPEZq_sK1Pcmqas7VPFS1BLw_N17k3m/view?usp=sharing',
    'https://drive.google.com/file/d/1tDfT6XdRkMWtNRUp9oBCcKSKb1ExF5NQ/view?usp=sharing',
    'https://drive.google.com/file/d/1SjY281RVxCTpkSoh5C1YM7UMw3NO87sy/view?usp=sharing',
    'https://drive.google.com/file/d/1C81b4wyDM9I0WzZSqtXn7C7qCpTGLjcf/view?usp=sharing',
    'https://drive.google.com/file/d/1FGeZLPltn1lnYxzMxNpHy2Ho2pNeWybG/view?usp=sharing',
    'https://drive.google.com/file/d/1FS-WadSEzfKbo_IiN6m2nxacG1xK4Uvm/view?usp=sharing',
    'https://drive.google.com/file/d/1sOnJ-sz11uz4fePpKkmF1sgVBXkuT0xZ/view?usp=sharing',
    'https://drive.google.com/file/d/1dtBfWdTTQmOpaHJM7ky4bd-HZTENWwvB/view?usp=sharing',
    'https://drive.google.com/file/d/113nqVLHzU732QiQV-45fiKYijLqLkOal/view?usp=sharing',
    'https://drive.google.com/file/d/1j0ygsE6WmL3XTjI372PZ3nB3EgAijOvy/view?usp=sharing',
    'https://drive.google.com/file/d/1XsMSgr7JSYAdemoIfCHjL5JAVusEsz_w/view?usp=sharing',
    'https://drive.google.com/file/d/1hnPujp9Sa1by15szbNBewkecTkPcpBvD/view?usp=sharing',
    'https://drive.google.com/file/d/1lNodE9XCBuTsrQ8SQnCs5-UILlSlVHAt/view?usp=sharing',
    'https://drive.google.com/file/d/1oRCn9ySf2svJdUjz4KFozNlOqaR141IL/view?usp=sharing',
    'https://drive.google.com/file/d/10QOVWQOKe-_cJVpRr42hdW9mmUh6qOMc/view?usp=sharing',
    'https://drive.google.com/file/d/1300IPvyPnpQhvyEbjLtYCGpmivHXwFbv/view?usp=sharing',
    'https://drive.google.com/file/d/1VrGRiwXZSzyKzSKYH0_ee5JUIdWvXGFz/view?usp=sharing',
    'https://drive.google.com/file/d/1FTu1M-PBq_6Mh2GCVDVseCptiTDuy-Vg/view?usp=sharing',
    'https://drive.google.com/file/d/17eHT4E2f67-ORjkiNaNIFSshr0i7n9HJ/view?usp=sharing',
    'https://drive.google.com/file/d/1AUjU77Oto5ZysQz_fngH7RYSX8ZI5vvx/view?usp=sharing',
    'https://drive.google.com/file/d/1BYPj0kIR6k2WpSil6YKe1q40tzvg72oe/view?usp=sharing',
    'https://drive.google.com/file/d/1hZm9YbOyKMfusYnhUdTqgmWOwKbaZ5lX/view?usp=sharing',
    'https://drive.google.com/file/d/171sy1zOwoqrmfzuYTUlEDMs2qkt78i8g/view?usp=sharing',
    'https://drive.google.com/file/d/1QZpbtvDDGQbvthmEzsgkN4V7nqpkgZ2P/view?usp=sharing',
    'https://drive.google.com/file/d/1AHuuFG21nrIhniEVbQexiAX7mGY_aFYV/view?usp=sharing',
    'https://drive.google.com/file/d/1VASN3e2LsFT6IIF5gG0vay8dwvOFax5i/view?usp=sharing',
    'https://drive.google.com/file/d/1zCpioDzfQMNMT7OLYuNySC-vn_aMjXGZ/view?usp=sharing',
    'https://drive.google.com/file/d/1CXH57yz2HCKfa2yPoR5z1NILL_Z6yBi7/view?usp=sharing',  
    'https://drive.google.com/file/d/1NDPwPkVpsd9O8jIhqzhTHKM5-JQlTvD3/view?usp=sharing',
    'https://drive.google.com/file/d/1MyCQGoRmrR6eGsmA80p_gyNdE7_azuPc/view?usp=sharing',
    'https://drive.google.com/file/d/1z3W9zikejATKxCCMgKGz5UZaP5p3ZsxH/view?usp=sharing',
    'https://drive.google.com/file/d/1kTZ6N-BDTvrjFQX8V-m974ET5t4Zo2CD/view?usp=sharing',
    'https://drive.google.com/file/d/1Wuxcc3SOd4QBJiNFb_EEc5ZG67Z4iG1h/view?usp=sharing',
    'https://drive.google.com/file/d/1uUyskbR1Uv6Xyx8S0vFZHWqGPOLwHJJz/view?usp=sharing',
    'https://drive.google.com/file/d/1Ip-gpPtWk-4Og8u1uDWh7rjfI5ZhAY8X/view?usp=sharing',
    'https://drive.google.com/file/d/1_Yo-sEa9tDJD_CIPmWsXI4lF7CsVyNll/view?usp=sharing',
    'https://drive.google.com/file/d/16z2p--l8KOT54Glxm2DJLT3uiilZb5vS/view?usp=sharing',
    'https://drive.google.com/file/d/1U6rSvwt_zu1EQXRT7gf6xhtrOTE1hfOH/view?usp=sharing',
    'https://drive.google.com/file/d/1AjqJfsD-2Xn8_Pl31N2i2OY-j3-fWc1X/view?usp=sharing',
    'https://drive.google.com/file/d/17ujD-gHKm0b3hDF0svUQIQMXCtIxZkqK/view?usp=sharing',
    'https://drive.google.com/file/d/1QomTp2DOTjK6AB9lNW1qyvkwrZoEDf60/view?usp=sharing',
    'https://drive.google.com/file/d/1wiKqUe-YUDadMrS3vnbRd2Dto4RJKH65/view?usp=sharing',
    'https://drive.google.com/file/d/11UG-9fVDLoug0a_Kk0NJ5HdWo7i8aBMQ/view?usp=sharing',
    'https://drive.google.com/file/d/1Guzirc_GYWQoWsM1A7pWm81wPf0daTrV/view?usp=sharing',
    'https://drive.google.com/file/d/17DWbsN9NCdUlVdv1T2WgGK2TBElaTyRr/view?usp=sharing',
    'https://drive.google.com/file/d/1s4vqM8TL9-Sp9LwwdE6pO6EIJ33ZL5wq/view?usp=sharing',
    'https://drive.google.com/file/d/1SDCUvOM6LcYA3ZJtZMTtuhgjfvQ1lSHC/view?usp=sharing',
    'https://drive.google.com/file/d/1sik0E2e7mr1_h9pbUG2uTZCa3hvj79YE/view?usp=sharing',
    'https://drive.google.com/file/d/1ql_Y4x0d-igVY3dPNEbfa6F31YmqnhV1/view?usp=sharing',
    'https://drive.google.com/file/d/1BZeWSZB-UbSBQtTEZSZ46RBV485PjLxc/view?usp=sharing',
    'https://drive.google.com/file/d/1W_n7CPbwQZeKalqGg-FKqASN4jvJV8QG/view?usp=sharing',
    'https://drive.google.com/file/d/1ZqST1qsgwA-tS0mhs3ysGwbzPoEG9fNe/view?usp=sharing',
    'https://drive.google.com/file/d/1OdtLYR4Zv3VidYTCBfQ5DUne_Z9t9xU4/view?usp=sharing',
    'https://drive.google.com/file/d/1ZZOQPdqXyRYNt0ePXuDincaD2BUvtyQv/view?usp=sharing',
    'https://drive.google.com/file/d/1pH1A4MkkAaXn_gU1ozFpCR5Bovpv0sTV/view?usp=sharing',
    'https://drive.google.com/file/d/136d5DsyRb-fk27v7DNatZwKsDgdpSt6f/view?usp=sharing',
    'https://drive.google.com/file/d/1iu14MuZI2uJY9X4YQH-J5fyEODJaNhch/view?usp=sharing',
    'https://drive.google.com/file/d/19lvj24DAefxKC4GtxahOvVuNm5GP7sFN/view?usp=sharing',
    'https://drive.google.com/file/d/1Kibu8e3m7pw_ABQqnQ1q2csaUnKoxNTg/view?usp=sharing',
    'https://drive.google.com/file/d/1qoHkQnNw84DhAiP-t6sPT9yVkIfFXzib/view?usp=sharing',
    'https://drive.google.com/file/d/1gyyJ_mZWV0tPn5aBG57m2Gbx-I5DQtMn/view?usp=sharing',
    'https://drive.google.com/file/d/12K7MM16Vsa3aL8lynttSDYBV-jD_DcdZ/view?usp=sharing',
    'https://drive.google.com/file/d/1gaWej9P6yhXQB6Y_sCBubzP5JvBBCOTJ/view?usp=sharing',
    'https://drive.google.com/file/d/1J-mJBmXkDirYpawioqJ5SarEWdsanwG2/view?usp=sharing',
    'https://drive.google.com/file/d/1U8qyqrimFDUnjTVsFBLAhQ_Ujl2CjmKV/view?usp=sharing',
    'https://drive.google.com/file/d/1kd-wHLmT5OilpXZMkuQ1FbkW561agrxk/view?usp=sharing',
    'https://drive.google.com/file/d/1nkMJKHQM2QkcTkrC0It3TNuha-v-klz7/view?usp=sharing',
    'https://drive.google.com/file/d/1P_J2WKBzl_jzLI3OOvy0DrZmdbx7vA6n/view?usp=sharing',
    'https://drive.google.com/file/d/1dr5iP3A7gI7sDGHn8kpv2T53M3a6yTaQ/view?usp=sharing',
    'https://drive.google.com/file/d/1Pc-9jX_Upx4sXvgIKlsrkIpxfBcTXp7h/view?usp=sharing',
    'https://drive.google.com/file/d/1MMHqmqLvmNz-du6b3g92isNKtieAd5Li/view?usp=sharing',
    'https://drive.google.com/file/d/1Dx_aR2hj-8yMjo9Y8hjPR_I8gG2WQp7B/view?usp=sharing',
    'https://drive.google.com/file/d/1FXDms0Vefe6Va4lvtNkQt7y3thkUYCKL/view?usp=sharing',
    'https://drive.google.com/file/d/1FAF-WqJwiZVsyuoyJLFAJCwnMVUOpncO/view?usp=sharing',
    'https://drive.google.com/file/d/1AjEUnUHB1hMn-CUAJJLetCh8ndKoWxs4/view?usp=sharing',
    'https://drive.google.com/file/d/1Sv0dQ6PzA9ZVpzIRRKM_PycLo_V4SwIB/view?usp=sharing',
    'https://drive.google.com/file/d/1i--7leSY06UzvUIr5ZkRv4a5Jl4G4YA9/view?usp=sharing',
    'https://drive.google.com/file/d/1qzRt0GvcLspl6whVdKWFaAriB28AiWgp/view?usp=sharing',
    'https://drive.google.com/file/d/1gGFBIex48TV-23qW6y68ar7swrdprfvS/view?usp=sharing',
    'https://drive.google.com/file/d/1g5U8s1Sa9jkom3cRTGNik3c1OfrnT-9b/view?usp=sharing',
    'https://drive.google.com/file/d/1TPtcLRuePv5MqoCppn_pls3NjyZteQXV/view?usp=sharing',
    'https://drive.google.com/file/d/1WfWILZN4HzhoH1MQzYCov6FWUVv0UFso/view?usp=sharing',
    'https://drive.google.com/file/d/1I0Lh6bTz1HrvwIW9pXeTK198064nWMA5/view?usp=sharing',
    'https://drive.google.com/file/d/1dillo4G3wFjHVPVWXvCJNLKlTbLuX_5-/view?usp=sharing',
    'https://drive.google.com/file/d/1K1HIs-ESv1mW-dDdcnSfVyEMti2-zrdW/view?usp=sharing',
    'https://drive.google.com/file/d/1zwpSzml658wXPCdpeiCYtP3qlne_PPYX/view?usp=sharing',
    'https://drive.google.com/file/d/1eBkjGNdTHNeHbLRn_fWFtRIugCysbu4W/view?usp=sharing',
    'https://drive.google.com/file/d/1VIK735btN7xFWRWRRIHClBWnMkTENH_3/view?usp=sharing',
    'https://drive.google.com/file/d/1KQ1jbYao4v2x-2j_tJ65z-gKmnMLEtiI/view?usp=sharing',
    'https://drive.google.com/file/d/1vUNAHmBg1tly49gzwFJHBSG_35_Lr6tc/view?usp=sharing',
    'https://drive.google.com/file/d/1smjAlQrrY9HipbGv_SqWorQeKPeNrjqk/view?usp=sharing',
    'https://drive.google.com/file/d/1fLrZNSnPM4bRaUq-S5RPmQ_2vU032Kh0/view?usp=sharing',  
    'https://drive.google.com/file/d/1mi-i1twIjtPiYsuTXKHs4VDrGQcLehKH/view?usp=sharing',
    'https://drive.google.com/file/d/1tzjQ-OaL873pfVClZpH_O9KF1amm40QL/view?usp=sharing',
    'https://drive.google.com/file/d/1reB7Um1YCz2EMZpy38j4vg7xTXu9UVuV/view?usp=sharing',
    'https://drive.google.com/file/d/1qwNAY1UgQPVU51VnL83WA27CmIxHKWAy/view?usp=sharing',
    'https://drive.google.com/file/d/1-a2HPP9E3Nko7tzVuI9ACzzEYBJRPwJ4/view?usp=sharing',
    'https://drive.google.com/file/d/1NFpjEYjcL-vlPZijSnHdV_x5NJTZONO5/view?usp=sharing',
    'https://drive.google.com/file/d/1Iy0gNHccCQU-4O1iRPa_HMGzFOyCwTOm/view?usp=sharing',
    'https://drive.google.com/file/d/1afiX9wsHaMh2dQ-1ZsPU5QctQl0zwR6F/view?usp=sharing',
    'https://drive.google.com/file/d/1YMS1YtK0Y0SJU8uANLBwUEZ7Hvba6Z25/view?usp=sharing',
    'https://drive.google.com/file/d/14DpEzl3y4qgqG4dNr4w_mDJLHOo9CAYv/view?usp=sharing',
    'https://drive.google.com/file/d/1lemVKWJfDLDis-xUxIktYK0jUy5XOQgR/view?usp=sharing',
    'https://drive.google.com/file/d/1kfBdaq1ZCbBxy6P1jR4PF3BxehOVd0RI/view?usp=sharing',
    'https://drive.google.com/file/d/186XjZvso9fKRuhxXbdXiLJYdKoLoR2OM/view?usp=sharing',
    'https://drive.google.com/file/d/1hYZNLfb4lUAUN5yaGnspRlBiUD4QFwoV/view?usp=sharing',
    'https://drive.google.com/file/d/1EMs4AlzVIcgrkqeg26zWlO_3BXoaitQV/view?usp=sharing',
    'https://drive.google.com/file/d/1HOiLLeYNHA7Sar6aUtzPvzbcXzoozVvl/view?usp=sharing',
    'https://drive.google.com/file/d/1GXEowR8kyNTsFIOK-07hZJ1Ssup_z516/view?usp=sharing',
    'https://drive.google.com/file/d/1tfveZxZ04pfgGIjqjASyxueZCfLYL-ag/view?usp=sharing',
    'https://drive.google.com/file/d/1mN-URS7UiQ62VaLTUaAd0-7Kwhfng2_6/view?usp=sharing', 
    'https://drive.google.com/file/d/1ODrC4Pyuj23--dqD5-6BolL7ka9CwCp6/view?usp=sharing',
    'https://drive.google.com/file/d/1U1GwlZijMHstKcsX8S3G_ClWO9V9-oN3/view?usp=sharing',
    'https://drive.google.com/file/d/1Pz8Ga9oFOyVPUbb-hNv7wg5TRFR2sILe/view?usp=sharing',
    'https://drive.google.com/file/d/1V_ji01MGhix1PSi3NDmVDWYbFxcQaigX/view?usp=sharing',
    'https://drive.google.com/file/d/17JCekqFcqmE6mi1vychR2pb0bzLQYcWj/view?usp=sharing',
    'https://drive.google.com/file/d/1dPZrAzm9Ve9hnMC_Ygh77sVGuhPO1fzt/view?usp=sharing',
    'https://drive.google.com/file/d/1GdjwQxoq98igt9Cc6-Y3i19kSXZq_BOL/view?usp=sharing',
    'https://drive.google.com/file/d/1C7KU3fijb15mA1KZHeohcnQqTLHc0xbK/view?usp=sharing',
    'https://drive.google.com/file/d/12oHeg7gWfyvMH7Ffh5r5pjq3HoZP_HgU/view?usp=sharing',
    'https://drive.google.com/file/d/1rVv04H12IrYIx_7MFeqn7s1X4pEY8hlP/view?usp=sharing',
    'https://drive.google.com/file/d/1FlQNqkNmFs8cDqOMQJiYzpOS5QdWNAdI/view?usp=sharing',
    'https://drive.google.com/file/d/1flFBLg5sT3qzrlR5cr8GVhz_xO-39I-d/view?usp=sharing',
    'https://drive.google.com/file/d/1xsCreJHSf5rimwzmTXHoEO1fZyi9K5MC/view?usp=sharing',
    'https://drive.google.com/file/d/1ucmwaViYotJu8UvZnF7tD8J97obiO3p2/view?usp=sharing',
    'https://drive.google.com/file/d/1QmAdP7o5jbP17K_v4F5J-41DP03RyXir/view?usp=sharing',
    'https://drive.google.com/file/d/1t7fMCUDaBqBpvDIUZWcaW4wYljpTIq9A/view?usp=sharing',
    'https://drive.google.com/file/d/18tG22fWzB1cockR_TfYvc1qETyGUWsj2/view?usp=sharing',
    'https://drive.google.com/file/d/11PpfObWBe6reaMLa-jyLhFFUprQMvcW6/view?usp=sharing',
    'https://drive.google.com/file/d/1-8FZhGnT9UQNuKBCuSAwnIOhXkqHUXli/view?usp=sharing',
    'https://drive.google.com/file/d/12n19TI68kOChl3DBZvKCNXLBBEABkJfk/view?usp=sharing',
    'https://drive.google.com/file/d/1vN-cuD0V-w3gTrec_3o47pyBwrkaz0YD/view?usp=sharing',
    'https://drive.google.com/file/d/1scj-ffybekxvpRgWZyqPe9nZnkTYBmgG/view?usp=sharing',
    'https://drive.google.com/file/d/1zqdxTebBVaRsV3aZOR_ZtNY3CKW_kyGT/view?usp=sharing',
    'https://drive.google.com/file/d/1D72iNFxZDO73p-wruRZmrhl2YmB_v--j/view?usp=sharing',
    'https://drive.google.com/file/d/1RITUVedV1C4ZYs18E69HdQBuyirTY1Ao/view?usp=sharing',
    'https://drive.google.com/file/d/18SECGGNy769KqKfG-jgzOWPhUmu0B-N8/view?usp=sharing',
    'https://drive.google.com/file/d/1IKJ0CObHIGpX5w8yBfvUob723G_LZTPr/view?usp=sharing',
]

fcvid_id = []




def download_from_google(token_id, filename):
    r"""Downloads desired filename from Google drive"""
    print('Downloading %s ...' % os.path.basename(filename))
    url = 'https://docs.google.com/uc?export=download'
    destination = filename + '.tar'
    session = requests.Session()
    response = session.get(url, params={'id': token_id}, stream=True)
    print(response.headers)

    token = get_confirm_token(response)
    if token:
        params = {'id': token_id, 'confirm': token}
        response = session.get(url, params=params, stream=True)
    
    save_response_content(response, destination)
    print(destination)
    file = tarfile.open(destination, 'r:')
    print("Extracting %s ..." % destination)
    file.extractall(filename)
    file.close()
    os.remove(destination)
    os.rename(filename, filename + '_tmp')
    os.rename(os.path.join(filename + '_tmp', os.path.basename(filename)), filename)
    os.rmdir(filename+'_tmp')
    
# def download_file_from_google_drive(id_, destination):
#     URL = "https://docs.google.com/uc?export=download"

#     session = requests.Session()
#     response = session.get(URL, params = { 'id' : id_ }, stream = True)
#     token = get_confirm_token(response)
#     if token:
#         params = { 'id' : id_, 'confirm' : token }
#         response = session.get(URL, params = params, stream = True)
    
#     print("here")
#     print(response.headers['Content-Disposition'])
# #     basename = response.headers['Content-Disposition'].split(';')[1].split('filename=')[1].replace('\"', '')
#     basename = 'r'
#     full_dst_filenname = pth.join(destination, basename)
#     save_response_content(response, full_dst_filenname)
#     return full_dst_filenname    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None
    

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    
    
    
if __name__ == '__main__':
    
    filename_list = []
#    destination = '/MD1400/jhseon/datasets/fcvid'
    destination = '/data/datasets/fcvid'
    os.makedirs(destination, exist_ok=True)
    err_cnt = 0
    target_url_list = minik_txt_url_list
#     target_url_list = fcvid_url_list
    for target_url in target_url_list:
        token = re.split('/', target_url)[5]
        print(token)
        try:
            download_from_google(token, destination+'/' + token)
        except:
            err_cnt += 1
            print("error : %d, total : %d" %(err_cnt, len(target_url_list)))
    
#     print(fcvid_id)
#     download_func = partial(download_file_from_google_drive, destination=destination)
#     with Pool(4) as pool:
#         for i, filename in tqdm(enumerate(pool.imap_unordered(download_func, fcvid_id)), total=len(fcvid_id)):
#             print('{} is done!'.format(filename))
#             filename_list.append(filename)
    
#     zip_filename_list = [filename for filename in filename_list if filename.endswith('.zip')]
    
#     for zip_filename in tqdm(zip_filename_list):
#         with zipfile.ZipFile(zip_filename) as target_zip:
#             dest_path = pth.splitext(zip_filename)[0]
#             os.makedirs(dest_path, exist_ok=True)
#             target_zip.extractall(dest_path)
#             print('{} is done!'.format(dest_path))

    

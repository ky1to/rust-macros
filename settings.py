# -*- coding: utf-8 -*-

class Settings:
    path_tesseract = "C:/Program Files/Tesseract-OCR/tesseract.exe" # change it to yours  
    btn_start = "f3"
    btn_off = "u"
    weapon_pattern = {
                "МР5А4": {
                    "normal":{
                        "Text": "MP5",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 6,
                                "Time1": 0.011
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.010
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.008
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.011
                            }
                        }
                    },
                    "holo":{
                        "Text": "МР5А4 (holo)",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 8,
                                "Time1": 0.012
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 6,
                                "Time1": 0.012
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 4,
                                "Time1": 0.012
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 4,
                                "Time1": 0.015
                            }
                        }
                    }
                },
        
                "САМОДЕЛЬНЫЙ ПИСТОЛЕТ-ПУЛЕМЕТ": {
                    "normal":{
                        "Text": "SMG",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 2,
                                "Time1": 0.008
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 2,
                                "Time1": 0.008
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 2,
                                "Time1": 0.008
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 2,
                                "Time1": 0.008
                            }
                        }
                    },
                    "holo":{
                        "Text": "SMG (holo)",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.008
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.008
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.008
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.008

                            }
                        }
                    }
                },
                "ПИСТОЛЕТ-ПУЛЕМЕТ ТОМПСОНА": {
                    "normal":{
                        "Text": "Tomson",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.015
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.02
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 2,
                                "Time1": 0.015
                            }
                        }
                    },

                    "holo":{
                        "Text": "Tomson (holo)",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015

                            }
                        }
                    }
                },

                "ШТУРМОВАЯ ВИНТОВКА 18-300": {
                    "normal":{
                        "Text": "LR-300",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 13,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 13,
                                "Time1": 0.015
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 8,
                                "Time1": 0.02
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.015
                            }
                        }
                    },

                    "holo":{
                        "Text": "LR-300 (holo)",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 3,
                                "Time1": 0.015

                            }
                        }
                    }
                },


                "ПОЛУАВТОМАТИЧЕСКАЯ ВИНТОВКА": {
                    "normal":{
                        "Text": "Berdanka",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 4,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 4,
                                "Time1": 0.015
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 6,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 4,
                                "Time1": 0.015
                            }
                        }
                    },

                    "holo":{
                        "Text": "Berdanka (holo)",
                        "got_up": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.015
                            }
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.015
                            },
                            "hip" : {
                                "X": 0,
                                "Y": 5,
                                "Time1": 0.015

                            }
                        }
                    }
                },

                "ШТУРМОВАЯ ВИНТОВКА": {
                    "normal":{
                        "Text": "AK47",
                        "got_up": {
                            "taking_aim": {
                                "X": -5,
                                "Y": 15,
                                "X2": -11, 
                                "Y2": 16,
                                "Time1": 0.019,
                                "Time2": 0.016, 
                                "Tick": 13
                            },
                            "hip": {
                                "X": -3,
                                "Y": 10,
                                "X2": -7, 
                                "Y2": 10,
                                "Time1": 0.027,
                                "Time2": 0.027, 
                                "Tick": 13
                            },
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": -3,
                                "Y": 10,
                                "X2": -9, 
                                "Y2": 11,
                                "Time1": 0.04,
                                "Time2": 0.042, 
                                "Tick": 13
                            },
                            "hip": {
                                "X": -2,
                                "Y": 6,
                                "X2": -5, 
                                "Y2": 6,
                                "Time1": 0.04,
                                "Time2": 0.044, 
                                "Tick": 13
                            },
                        }
                    },

                    "holo":{
                        "Text": "AK47 (holo)",
                        "got_up": {
                            "taking_aim": {
                                "X": -3,
                                "Y": 13,
                                "X2": -10, 
                                "Y2": 14,
                                "Time1": 0.014,
                                "Time2": 0.01, 
                                "Tick": 60
                            },
                            "hip": {
                                "X": -2,
                                "Y": 6,
                                "X2": -5, 
                                "Y2": 6,
                                "Time1": 0.035,
                                "Time2": 0.035, 
                                "Tick": 13
                            },
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": -4,
                                "Y": 12,
                                "X2": -10, 
                                "Y2": 13,
                                "Time1": 0.04,
                                "Time2": 0.036, 
                                "Tick": 13
                            },
                            "hip": {
                                "X": -2,
                                "Y": 6,
                                "X2": -5, 
                                "Y2": 6,
                                "Time1": 0.035,
                                "Time2": 0.035, 
                                "Tick": 13
                            },
                        }
                    },
                    "x8":{
                        "Text": "AK47 (x8)",
                        "got_up": {
                            "taking_aim": {
                                "X": -3,
                                "Y": 12,
                                "X2": -8, 
                                "Y2": 12,
                                "Time1": 0.014,
                                "Time2": 0.008, 
                                "Tick": 60
                            },
                            "hip": {
                                "X": -2,
                                "Y": 6,
                                "X2": -5, 
                                "Y2": 6,
                                "Time1": 0.035,
                                "Time2": 0.035, 
                                "Tick": 13
                            },
                        },
                        "sitting": {
                            "taking_aim": {
                                "X": -6,
                                "Y": 37,
                                "X2": -25, 
                                "Y2": 37,
                                "Time1": 0.01,
                                "Time2": 0.01, 
                                "Tick": 40
                            },
                            "hip": {
                                "X": -2,
                                "Y": 6,
                                "X2": -5, 
                                "Y2": 6,
                                "Time1": 0.035,
                                "Time2": 0.035, 
                                "Tick": 13
                            },
                        }
                    }
                },
            }
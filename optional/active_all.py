import active_deactive_mail_check

# active_deactive_mail_check.check_active_special('total_active_inactive_list.txt', 'active_all_2.txt')
active_deactive_mail_check.checkActiveInactiveCorrupted('total_active_inactive_list.txt',
                                                        '/output/active_all_3.txt',
                                                        '/output/inactive_all_3.txt',
                                                        '/output/corrupt_all_3.txt',
                                                        1, 3000)
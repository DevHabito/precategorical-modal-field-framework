from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class IntegrityTests(unittest.TestCase):
    def test_registry_results_pass(self):
        reg=json.loads((ROOT/'audit_registry.json').read_text())
        self.assertTrue(reg)
        for e in reg:
            d=json.loads((ROOT/'results'/e['result']).read_text())
            self.assertTrue(d['verdict'].startswith('PASS'))
            g=d.get('gates')
            if isinstance(g,dict): self.assertTrue(all(v is True for v in g.values()))
            else: self.assertEqual(d['pass_count'],d['gate_count'])
    def test_all_json_valid(self):
        for p in (ROOT/'results').glob('*.json'): json.loads(p.read_text())
    def test_notes_present(self):
        for e in json.loads((ROOT/'audit_registry.json').read_text()):
            if e.get('note'): self.assertTrue((ROOT/'docs'/'technical_notes'/e['note']).exists())
    def test_figures_present(self):
        self.assertGreater(len(list((ROOT/'figures').glob('*.png'))),0)
    def test_a79_nested_certificates(self):
        d=json.loads((ROOT/'results'/'a79_compression_interval_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_COMPRESSION_INTERVALS_AND_CONTACT_ENTRY_POLYNOMIALS')
        self.assertEqual(d['nested_support_gate_count'],48)
        self.assertEqual(d['nested_support_pass_count'],48)
        for item in d['support_results']:
            self.assertTrue(all(v is True for v in item['gates'].values()))
    def test_a79_polynomial_hashes(self):
        import hashlib
        d=json.loads((ROOT/'results'/'a79_boundary_polynomials.json').read_text())
        self.assertEqual(len(d['polynomials']),6)
        for item in d['polynomials']:
            coeffs=item['polynomial']['coefficients_descending']
            canonical=json.dumps(coeffs,separators=(',',':'))
            digest=hashlib.sha256(canonical.encode('utf-8')).hexdigest()
            self.assertEqual(digest,item['polynomial']['coefficient_sha256'])
    def test_a80_local_atlas(self):
        d=json.loads((ROOT/'results'/'a80_local_compression_window_atlas_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_LOCAL_COMPRESSION_WINDOW_ATLAS_AND_SIX_TERM_BOUNDARY_LAW')
        self.assertEqual(d['exact_compression_window_count'],20)
        self.assertEqual(d['windows_containing_s0'],[40,57,74])
        self.assertEqual(d['total_nonboundary_interval_KKT_conditions'],1888)
        self.assertTrue(all(v is True for v in d['gates'].values()))
        certificates=json.loads((ROOT/'results'/'a80_interval_KKT_condition_certificates.json').read_text())
        self.assertEqual(certificates['condition_certificate_count'],1888)
        self.assertTrue(all(item['certificate']['pass'] is True for item in certificates['certificates']))
    def test_a80_boundary_polynomial_hashes_and_sparsity(self):
        import hashlib
        d=json.loads((ROOT/'results'/'a80_boundary_polynomial_catalogue.json').read_text())
        self.assertEqual(d['polynomial_count'],142)
        for item in d['polynomials']:
            self.assertEqual(item['polynomial']['term_count'],6)
            coefficient_map=item['polynomial']['nonzero_coefficients_by_exponent']
            degree=item['polynomial']['degree']
            coefficients=['0']*(degree+1)
            for exponent,value in coefficient_map.items():
                coefficients[degree-int(exponent)]=value
            canonical=json.dumps(coefficients,separators=(',',':'))
            digest=hashlib.sha256(canonical.encode('utf-8')).hexdigest()
            self.assertEqual(digest,item['polynomial']['coefficient_sha256'])
    def test_a81_reduced_boundary_system(self):
        d=json.loads((ROOT/'results'/'a81_reduced_boundary_system_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_REDUCED_BOUNDARY_SYSTEM_AND_ORDERED_ROOT_THEOREM')
        self.assertEqual(d['contract']['all_admissible_pair_count'],1438)
        self.assertEqual(d['selected_contact_theorem']['root_class_counts'],{
            'complete_ordered_pair':20,
            'upper_only':3,
            'lower_only':0,
            'none':48,
            'other':0,
        })
        self.assertEqual(d['primitive_normalization_result']['asymmetry_supports'],[34,64,69,77])
        self.assertTrue(all(v is True for v in d['gates'].values()))
    def test_a81_positive_gap_certificates(self):
        d=json.loads((ROOT/'results'/'a81_all_contact_positive_gap_certificates.json').read_text())
        self.assertEqual(d['pair_count'],1438)
        self.assertTrue(d['all_T_positive'])
        self.assertTrue(d['all_Delta_positive'])
        self.assertEqual(len(d['certificates']),1438)
        self.assertTrue(all(item['positive_boundary_gap'] for item in d['certificates']))
        self.assertTrue(all(item['positive_scaled_mass_t'] for item in d['certificates']))
    def test_a81_selected_formula_records(self):
        d=json.loads((ROOT/'results'/'a81_selected_contact_coefficient_formulas.json').read_text())
        self.assertEqual(d['record_count'],71)
        for item in d['records']:
            for boundary in ('lower','upper'):
                self.assertEqual(len(item['cofactor_coefficients'][boundary]['six_coefficients']),6)
    def test_a82_adjacent_contact_locator(self):
        d=json.loads((ROOT/'results'/'a82_adjacent_contact_locator_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_ADJACENT_CONTACT_LOCATOR_AND_LOCAL_ORIENTATION_SWITCHES')
        self.assertEqual(d['probe_theorem']['compressed_contact_count'],1438)
        self.assertEqual(d['probe_theorem']['adjacent_comparison_count'],1367)
        self.assertEqual(d['probe_theorem']['strict_unimodal_support_count'],71)
        self.assertEqual(d['probe_theorem']['classification_counts'],{
            'gamma_plus':57,
            'gamma_minus':11,
            'compressed':3,
            'invalid':0,
        })
        self.assertEqual(d['probe_theorem']['selection_matches_A78_count'],71)
        self.assertEqual(d['probe_theorem']['predicted_full_KKT_pass_count'],71)
        self.assertEqual(
            [item['maximum'] for item in d['probe_theorem']['compressed_maximizer_primal_feasibility_exceptions']],
            [23,28,34,45,51,56,62,68],
        )
        transitions=d['local_interval_extension']['certified_transitions']
        self.assertEqual([(item['maximum'],item['contact_pair']) for item in transitions],[
            (28,[6,7]),
            (79,[15,16]),
        ])
        self.assertTrue(all(item['simple_root_certificate']['pass'] for item in transitions))
        self.assertTrue(all(v is True for v in d['gates'].values()))
    def test_a82_adjacent_difference_catalogue(self):
        d=json.loads((ROOT/'results'/'a82_adjacent_difference_catalogue.json').read_text())
        self.assertEqual(d['polynomial_count'],1367)
        self.assertEqual(len(d['polynomials']),1367)
        crossing=[item for item in d['polynomials'] if item['endpoint_signs']['local_lower']!=item['endpoint_signs']['local_upper']]
        self.assertEqual([(item['maximum'],item['lower_contact']) for item in crossing],[(28,6),(79,15)])
        self.assertTrue(all(item['s0_sign'] in (-1,1) for item in d['polynomials']))
    def test_a83_sparse_adjacent_sign_atlas(self):
        d=json.loads((ROOT/'results'/'a83_seven_term_adjacent_sign_atlas_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_SEVEN_TERM_ADJACENT_DIFFERENCE_FACTORIZATION_AND_COMPLETE_LOCAL_SIGN_ATLAS')
        self.assertEqual(d['complete_local_sign_atlas']['adjacent_factor_count'],1367)
        self.assertEqual(d['complete_local_sign_atlas']['sign_definite_no_root_count'],1365)
        self.assertEqual(d['complete_local_sign_atlas']['one_simple_root_count'],2)
        self.assertEqual(d['discrete_concavity_test']['positive'],1141)
        self.assertEqual(d['discrete_concavity_test']['negative'],155)
        self.assertEqual(d['discrete_concavity_test']['zero'],0)
        self.assertEqual(d['discrete_concavity_test']['fully_strictly_concave_supports'],[10,11,12,13,14,15])
        self.assertEqual(d['feasibility_boundary']['A82_compressed_maximizer_primal_exceptions'],[23,28,34,45,51,56,62,68])
        self.assertTrue(all(v is True for v in d['gates'].values()))
    def test_a83_sparse_factor_catalogue(self):
        d=json.loads((ROOT/'results'/'a83_seven_term_adjacent_factor_catalogue.json').read_text())
        self.assertEqual(d['polynomial_count'],1367)
        self.assertEqual(len(d['records']),1367)
        self.assertTrue(all(item['polynomial']['term_count']==7 for item in d['records']))
        roots=[(item['maximum'],item['lower_contact']) for item in d['records'] if item['root_class']=='one_simple_root']
        self.assertEqual(roots,[(28,6),(79,15)])
    def test_a84_k_space_stress(self):
        d=json.loads((ROOT/'results'/'a84_k_space_exponential_polynomial_stress_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_K_SPACE_EXPONENTIAL_POLYNOMIAL_REDUCTION_AND_FINITE_ONE_VARIATION_STRESS')
        self.assertEqual(d['finite_exact_stress']['support_count'],291)
        self.assertEqual(d['finite_exact_stress']['adjacent_pair_count'],21607)
        self.assertEqual(d['finite_exact_stress']['pair_probe_exact_evaluation_count'],64821)
        self.assertEqual(d['finite_exact_stress']['strict_single_variation_sequence_count'],873)
        self.assertEqual(d['finite_exact_stress']['endpoint_crossing_factor_count'],51)
        self.assertEqual(d['analytic_k_space_reduction']['coefficient_variation_count'],7)
        self.assertEqual(d['analytic_k_space_reduction']['coefficient_sign_pattern'],[1,-1,1,1,-1,-1,1,-1,1,-1])
        self.assertTrue(all(v is True for v in d['gates'].values()))
    def test_a84_probe_catalogue(self):
        d=json.loads((ROOT/'results'/'a84_probe_contact_and_crossing_catalogue.json').read_text())
        self.assertEqual(len(d['support_records']),291)
        self.assertEqual(len(d['endpoint_crossings']),51)
        self.assertEqual(len(d['probe_contact_blocks']),51)
        self.assertTrue(all(all(item['strict_single_variation'].values()) for item in d['support_records']))
    def test_a85_dominant_balance_results(self):
        d=json.loads((ROOT/'results'/'a85_parity_dominant_balance_contact_localization_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_PARITY_DOMINANT_BALANCE_AND_ASYMPTOTIC_CONTACT_LOCALIZATION')
        finite=d['finite_exact_transition_balance']
        self.assertEqual(finite['exact_evaluation_count'],1746)
        self.assertEqual(finite['four_term_sign_mismatch_count'],1)
        self.assertEqual(finite['four_term_dominance_failure_count'],2)
        self.assertEqual(finite['eight_term_sign_mismatch_count'],0)
        self.assertEqual(finite['eight_term_dominance_failure_count'],0)
        diagnostic=d['high_precision_asymptotic_diagnostic']
        self.assertEqual(diagnostic['record_count'],864)
        self.assertEqual(diagnostic['within_one_contact_count'],864)
        self.assertTrue(all(v is True for v in d['gates'].values()))
    def test_a85_transition_catalogue(self):
        d=json.loads((ROOT/'results'/'a85_transition_dominant_balance_catalogue.json').read_text())
        self.assertEqual(len(d['transition_records']),873)
        self.assertEqual(len(d['four_term_failures']['sign']),1)
        self.assertEqual(len(d['four_term_failures']['dominance']),2)
        self.assertEqual(len(d['predictor_parameters']),3)
        self.assertEqual(
            (d['four_term_failures']['sign'][0]['maximum'],d['four_term_failures']['sign'][0]['probe_name'],d['four_term_failures']['sign'][0]['contact']),
            (12,'local_lower',3),
        )
    def test_a86_exact_rational_contact_strip(self):
        d=json.loads((ROOT/'results'/'a86_exact_rational_contact_strip_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_RATIONAL_THREE_CONTACT_LOCALIZATION_AND_FINITE_EXCLUSION_THRESHOLDS')
        self.assertEqual(d['finite_exact_contact_strip']['record_count'],873)
        self.assertEqual(d['finite_exact_contact_strip']['ceil_offset_counts'],{
            'local_lower':{'0':1,'1':65,'2':225},
            'probe':{'0':1,'1':105,'2':185},
            'local_upper':{'0':1,'1':133,'2':157},
        })
        self.assertEqual(d['finite_exact_delta_thresholds']['probe']['1/50']['smallest_verified_tail_start'],132)
        self.assertEqual(d['search_compression']['full_adjacent_contact_probe_count'],64821)
        self.assertTrue(all(v is True for v in d['gates'].values()))
        c=json.loads((ROOT/'results'/'a86_exact_rational_contact_strip_catalogue.json').read_text())
        self.assertEqual(c['record_count'],873)
        self.assertTrue(all(item['ceil_offset'] in (0,1,2) for item in c['records']))

    def test_a90_prethreshold_all_k_one_variation(self):
        d=json.loads((ROOT/'results'/'a90_prethreshold_all_k_one_variation_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_PRETHRESHOLD_NINE_PROBE_ALL_K_ONE_VARIATION_AND_FOUR_CONTACT_STRIP')
        finite=d['finite_exact_all_k_result']
        self.assertEqual(finite['support_probe_sequence_count'],4599)
        self.assertEqual(finite['adjacent_factor_evaluation_count'],594423)
        self.assertEqual(finite['strict_one_variation_sequence_count'],4599)
        self.assertEqual(finite['zero_factor_count'],0)
        strip=d['contact_strip_result']
        self.assertEqual(strip['offset_counts'],{'0':9,'1':1207,'2':3368,'3':15})
        self.assertEqual(strip['offset_three_count'],15)
        first=strip['first_offset_three_case']
        self.assertEqual((first['maximum'],first['probe'],first['base_contact_ceil_Mc'],first['maximizing_contact']),(325,'129/1000',55,58))
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a90_contact_sequence_catalogue(self):
        d=json.loads((ROOT/'results'/'a90_prethreshold_contact_sequence_catalogue.json').read_text())
        self.assertEqual(d['record_count'],4599)
        self.assertTrue(all(item['strict_one_variation'] for item in d['records']))
        self.assertTrue(all(item['zero_count']==0 for item in d['records']))
        self.assertTrue(all(item['ceil_offset'] in (0,1,2,3) for item in d['records']))


    def test_a91_exact_four_term_offset_three_mechanism(self):
        d=json.loads((ROOT/'results'/'a91_four_term_offset_three_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_FOUR_TERM_OFFSET_THREE_CLASSIFIER_AND_PARITY_SCREENING_OBSTRUCTION')
        exact=d['exact_four_term_reduction']
        self.assertEqual(exact['eligible_cell_count'],4563)
        self.assertEqual(exact['boundary_excluded_cell_count'],36)
        self.assertEqual(exact['four_core_positive_count'],15)
        self.assertEqual(exact['four_core_negative_count'],4548)
        self.assertEqual(exact['sign_mismatch_count'],0)
        self.assertEqual(exact['dominance_failure_count'],0)
        self.assertEqual(exact['offset_three_classifier_mismatch_count'],0)
        self.assertEqual(d['parity_corrected_locator_diagnostic']['screened_cell_count'],69)
        self.assertEqual(d['parity_corrected_locator_diagnostic']['false_positive_count'],54)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a91_four_term_catalogue(self):
        d=json.loads((ROOT/'results'/'a91_four_term_offset_three_catalogue.json').read_text())
        self.assertEqual(d['record_count'],4563)
        self.assertEqual(len(d['records']),4563)
        self.assertEqual(len(d['boundary_excluded_records']),36)
        self.assertTrue(all(item['four_core_sign']==item['full_sign'] for item in d['records']))
        self.assertTrue(all(item['four_core_strictly_dominates_residual'] for item in d['records']))
        self.assertEqual(sum(item['offset_three_exact'] for item in d['records']),15)
        self.assertEqual(len(d['parity_predictor_offset_three_screen']),69)


    def test_a92_exact_continuum_offset_three_windows(self):
        d=json.loads((ROOT/'results'/'a92_continuum_offset_three_window_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_CONTINUUM_DECISIVE_FACTOR_ATLAS_AND_25_LOCAL_OFFSET_THREE_WINDOWS')
        summary=d['summary']
        self.assertEqual(summary['nonempty_b_cell_count'],858)
        self.assertEqual(summary['negative_cell_count'],833)
        self.assertEqual(summary['full_positive_cell_count'],14)
        self.assertEqual(summary['single_root_cell_count'],11)
        self.assertEqual(summary['undecided_cell_count'],0)
        self.assertEqual(summary['local_window_count'],25)
        self.assertEqual(summary['new_supports_beyond_A91_nine_probe_grid'],[360,366,425,431,437,454,466,472,478,484])
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a92_continuum_catalogue(self):
        d=json.loads((ROOT/'results'/'a92_continuum_offset_three_window_catalogue.json').read_text())
        self.assertEqual(len(d['cells']),858)
        self.assertEqual(len(d['local_windows']),25)
        self.assertEqual(sum(item['classification']=='negative' for item in d['cells']),833)
        self.assertEqual(sum(item['classification']=='positive' for item in d['cells']),14)
        self.assertEqual(sum(item['classification']=='single_increasing_root' for item in d['cells']),11)
        self.assertTrue(all(item['strict_local_maximum_certified'] for item in d['local_windows']))
        self.assertTrue(all(item['equal'] for item in d['regressions']))

    def test_no_superseded_files_in_clean_package(self):
        forbidden={'a77_interval_contact_reset_certificate.py','a77_interval_contact_reset_results.json','_a75_fast_phase_test.py','_run_a75_m16_domain_roots.py'}
        present={p.name for p in ROOT.rglob('*') if p.is_file()}
        self.assertFalse(forbidden & present)

    def test_a87_exact_secant_classifier(self):
        d=json.loads((ROOT/'results'/'a87_exact_secant_offset_classifier_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_SECANT_RESIDUAL_THREE_OFFSET_CLASSIFIER_WITH_EIGHT_TERM_FALLBACK')
        self.assertEqual(d['exact_secant_classifier']['record_count'],873)
        self.assertEqual(d['exact_secant_classifier']['offset_counts'],{'0':3,'1':303,'2':567})
        self.assertEqual(d['exact_secant_classifier']['mismatch_count'],0)
        self.assertEqual(d['core_reductions']['four_term']['mismatch_count'],1)
        self.assertEqual(d['core_reductions']['eight_term']['mismatch_count'],0)
        self.assertEqual(d['global_monotonicity_obstruction']['negative_drop_count'],40483)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a87_catalogue_exact_classes(self):
        d=json.loads((ROOT/'results'/'a87_exact_secant_offset_classifier_catalogue.json').read_text())
        self.assertEqual(d['record_count'],873)
        self.assertEqual(len(d['records']),873)
        for item in d['records']:
            self.assertTrue(item['full_drop_positive'])
            self.assertTrue(item['eight_drop_positive'])
            self.assertEqual(item['full_predicted_offset'],item['true_offset'])
            self.assertEqual(item['eight_predicted_offset'],item['true_offset'])

    def test_a88_nine_term_secant_positivity(self):
        d=json.loads((ROOT/'results'/'a88_nine_term_secant_positivity_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_NINE_TERM_SECANT_REDUCTION_EXTENDED_EXACT_POSITIVITY_AND_POSITIVE_PARITY_PHASE_LIMIT')
        self.assertEqual(d['finite_exact_stress']['cell_count'],8019)
        self.assertEqual(d['finite_exact_stress']['nonpositive_full_secant_count'],0)
        self.assertEqual(d['finite_exact_stress']['four_term_core_sign_mismatch_count'],0)
        self.assertEqual(d['finite_exact_stress']['four_term_core_dominance_failure_count'],0)
        self.assertEqual(d['exact_nine_term_secant_reduction']['coefficient_sign_pattern'],[1,-1,1,1,-1,-1,1,-1,1])
        self.assertEqual(d['exact_nine_term_secant_reduction']['sign_variation_count'],6)
        self.assertTrue(d['parity_phase_asymptotic_limit']['even_positive'])
        self.assertTrue(d['parity_phase_asymptotic_limit']['odd_positive'])
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a88_catalogue(self):
        d=json.loads((ROOT/'results'/'a88_nine_term_secant_positivity_catalogue.json').read_text())
        self.assertEqual(d['record_count'],8019)
        self.assertEqual(len(d['records']),8019)
        self.assertTrue(all(item['full_secant_positive'] for item in d['records']))
        self.assertTrue(all(item['four_term_core_positive'] for item in d['records']))
        self.assertTrue(all(item['four_term_core_dominates'] for item in d['records']))

    def test_a89_uniform_secant_threshold(self):
        d=json.loads((ROOT/'results'/'a89_uniform_secant_threshold_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXPLICIT_UNIFORM_LOCAL_SECANT_POSITIVITY_THRESHOLD_M521')
        self.assertEqual(d['contract']['maximum_threshold'],521)
        self.assertEqual(d['proof_constants']['minimum_contact'],89)
        self.assertEqual(d['proof_constants']['beta_target_ratio_cap'],'1/32')
        self.assertTrue(float(d['proof_budget']['rounded_margin']['decimal'])>0)
        self.assertTrue(d['certificate_specific_threshold_transition']['M520_rounded_margin'].startswith('-'))
        self.assertEqual(d['regression']['cell_count'],45)
        self.assertTrue(d['regression']['all_positive'])
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a89_regression_catalogue(self):
        d=json.loads((ROOT/'results'/'a89_uniform_secant_threshold_catalogue.json').read_text())
        self.assertEqual(d['record_count'],45)
        self.assertEqual(len(d['records']),45)
        self.assertTrue(all(item['normalized_secant_positive'] for item in d['records']))
        self.assertEqual(sorted({item['maximum'] for item in d['records']}),[521,522,625,900,1000])


    def test_a93_continuum_global_one_variation(self):
        d=json.loads((ROOT/'results'/'a93_continuum_global_one_variation_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_FULL_SEQUENCE_CONTINUUM_ONE_VARIATION_AND_25_GLOBAL_OFFSET_THREE_WINDOWS')
        summary=d['summary']
        self.assertEqual(summary['selected_cell_count'],25)
        self.assertEqual(summary['full_positive_global_cell_count'],14)
        self.assertEqual(summary['simple_global_transition_cell_count'],11)
        self.assertEqual(summary['nondecisive_factor_certificate_count'],5426)
        self.assertEqual(summary['full_sequence_factor_classification_count'],5451)
        self.assertEqual(summary['interval_certificate_failure_count'],0)
        self.assertEqual(summary['independent_regression_count'],108)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a93_continuum_global_catalogue(self):
        d=json.loads((ROOT/'results'/'a93_continuum_global_one_variation_catalogue.json').read_text())
        self.assertEqual(d['window_count'],25)
        self.assertEqual(d['nondecisive_factor_certificate_count'],5426)
        self.assertEqual(d['full_sequence_factor_classification_count'],5451)
        self.assertEqual(d['regression_count'],108)
        self.assertEqual(d['failures']['interval_certificate_failures'],0)
        self.assertEqual(len(d['windows']),25)
        self.assertTrue(all(w['all_nondecisive_factors_certified'] for w in d['windows']))
        self.assertTrue(all(r['equal'] for r in d['regressions']))

    def test_a94_all_cell_continuum_one_variation(self):
        d=json.loads((ROOT/'results'/'a94_all_cell_continuum_one_variation_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_CONTINUUM_ALL_858_CELL_ONE_VARIATION_AND_205_GLOBAL_ADJACENT_TRANSITIONS')
        summary=d['summary']
        self.assertEqual(summary['cell_count'],858)
        self.assertEqual(summary['nondecisive_factor_classification_count'],124956)
        self.assertEqual(summary['full_sequence_factor_classification_count'],125814)
        self.assertEqual(summary['fixed_unique_global_cell_count'],653)
        self.assertEqual(summary['simple_adjacent_global_transition_cell_count'],205)
        self.assertEqual(summary['total_simple_root_count'],205)
        self.assertEqual(summary['strict_convexity_fallback_count'],12)
        self.assertEqual(summary['phase_counts'],{
            'unique_b_plus_1':195,
            'unique_b_plus_2':444,
            'b_plus_1_to_b_plus_2':193,
            'b_plus_2_to_b_plus_1':1,
            'unique_b_plus_3':14,
            'b_plus_2_to_b_plus_3':11,
        })
        self.assertEqual(summary['classification_failure_count'],0)
        self.assertEqual(summary['regression_failure_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a94_all_cell_continuum_catalogue(self):
        d=json.loads((ROOT/'results'/'a94_all_cell_continuum_one_variation_catalogue.json').read_text())
        self.assertEqual(d['summary']['cell_count'],858)
        self.assertEqual(d['summary']['nondecisive_factor_count'],124956)
        self.assertEqual(d['summary']['full_factor_count'],125814)
        self.assertEqual(d['summary']['direct_interval_certificate_count'],119984)
        self.assertEqual(d['summary']['exceptional_factor_record_count'],4972)
        self.assertEqual(len(d['cells']),858)
        self.assertTrue(all(item['one_variation_certified'] for item in d['cells']))
        self.assertTrue(all(item['remote_factor_signs_certified'] for item in d['cells']))
        reverse=[item for item in d['cells'] if item['phase_classification']=='b_plus_2_to_b_plus_1']
        self.assertEqual([(item['maximum'],item['base_contact']) for item in reverse],[(28,5)])
        self.assertEqual(d['regression_count'],48)
        self.assertTrue(all(item['equal'] for item in d['regressions']))
        self.assertEqual(d['failures']['classification_failures'],[])
        self.assertEqual(d['failures']['regression_failures'],[])

    def test_a95_rational_witness_lift_results(self):
        d=json.loads((ROOT/'results'/'a95_rational_witness_lift_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_RATIONAL_WITNESS_LIFT_ATLAS_AND_RESTRICTED_FAMILY_OBSTRUCTION')
        n=d['natural_lift_result']
        self.assertEqual(n['candidate_evaluation_count'],3189)
        self.assertEqual(n['unique_strict_lift_count'],980)
        self.assertEqual(n['no_strict_lift_count'],83)
        self.assertEqual(n['multiple_strict_lift_count'],0)
        self.assertEqual(n['pass_family_counts'],{
            'three_band_gamma_plus':922,
            'three_band_gamma_minus':18,
            'two_band_compressed':40,
        })
        self.assertEqual(n['obstruction_support_count'],75)
        self.assertEqual(n['obstruction_supports'][0],125)
        self.assertEqual(n['obstruction_supports'][-1],520)
        prefix=d['restricted_family_prefix_stress']
        self.assertEqual(prefix['obstruction_record_count'],29)
        self.assertEqual(prefix['candidate_count'],19421)
        self.assertEqual(prefix['strict_pass_count'],0)
        self.assertEqual(prefix['status_counts'],{
            'primal_infeasible':18323,
            'reduced_cost_infeasible':1069,
            'active_dual_infeasible':29,
        })
        self.assertEqual(d['first_obstruction']['maximum'],125)
        self.assertEqual(d['first_obstruction']['witness'],'33/250')
        self.assertEqual(d['first_obstruction']['full_restricted_catalogue']['candidate_count'],370)
        self.assertEqual(d['first_obstruction']['full_restricted_catalogue']['strict_pass_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a95_rational_witness_lift_catalogue(self):
        d=json.loads((ROOT/'results'/'a95_rational_witness_lift_catalogue.json').read_text())
        self.assertEqual(d['summary']['record_count'],1063)
        self.assertEqual(d['summary']['unique_strict_lift_count'],980)
        self.assertEqual(d['summary']['obstruction_count'],83)
        self.assertEqual(d['summary']['multiple_count'],0)
        self.assertEqual(d['summary']['prefix_exhaustive_record_count'],29)
        self.assertEqual(len(d['records']),1063)
        self.assertEqual(len(d['prefix_exhaustive_obstructions']),29)
        self.assertTrue(all(len(item['natural_lift_candidates'])==3 for item in d['records']))
        self.assertTrue(all(item['strict_pass_count'] in (0,1) for item in d['records']))
        self.assertTrue(all(item['strict_pass_count']==0 for item in d['prefix_exhaustive_obstructions']))


    def test_a95_chunked_replay_provenance(self):
        d=json.loads((ROOT/'provenance'/'a95_chunked_replay'/'a95_chunked_replay_manifest.json').read_text())
        self.assertEqual(d['verdict'],'PASS_CHUNKED_EXACT_REPLAY_PROVENANCE')
        self.assertEqual(d['natural_fragment_count'],30)
        self.assertEqual(d['natural_record_count'],1063)
        self.assertEqual(d['natural_unique_key_count'],1063)
        self.assertEqual(d['prefix_fragment_count'],5)
        self.assertEqual(d['prefix_record_count'],29)
        self.assertEqual(d['prefix_candidate_count'],19421)
        self.assertTrue(d['all_prefix_strict_pass_counts_zero'])


    def test_a96_full_lp_active_set_resolution(self):
        d=json.loads((ROOT/'results'/'a96_full_lp_active_set_resolution_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M125')
        self.assertEqual(d['resolved_active_set']['P_support'],[23,24,125])
        self.assertEqual(d['resolved_active_set']['Q_support'],[1,62,63])
        self.assertEqual(d['resolved_active_set']['active_bands'],[['alpha',1],['beta',-1]])
        k=d['strict_KKT_certificate']
        self.assertEqual(k['strict_condition_count'],259)
        self.assertEqual(k['unrestricted_atom_reduced_cost_count'],246)
        self.assertTrue(k['primal_objective_equals_dual_objective'])
        self.assertTrue(k['unique_global_basic_optimum'])
        self.assertTrue(all(v is True for v in d['gates'].values()))
        c=json.loads((ROOT/'results'/'a96_full_lp_active_set_certificate.json').read_text())
        self.assertEqual(len(c['reduced_costs']),246)
        self.assertTrue(all(item['sign']==1 for item in c['reduced_costs']))
        self.assertTrue(all(item['sign']==1 for item in c['inactive_band_slacks']))
        self.assertTrue(c['objective']['equal'])
        p=json.loads((ROOT/'provenance'/'a96_high_precision_active_set_discovery.json').read_text())
        self.assertEqual(p['discovered_active_set']['P_support'],[23,24,125])
        self.assertEqual(p['discovered_active_set']['Q_support'],[1,62,63])


    def test_a97_endpoint_released_interval_and_obstruction_results(self):
        d=json.loads((ROOT/'results'/'a97_endpoint_released_interval_and_obstruction_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_ENDPOINT_RELEASED_M125_INTERVAL_AND_76_OF_83_OBSTRUCTION_RESOLUTION_WITH_SEVEN_Q0_ENTRY_RESIDUALS')
        interval=d['M125_interval_theorem']
        self.assertTrue(interval['pass'])
        self.assertEqual(interval['complete_sign_census']['condition_count'],259)
        self.assertEqual(interval['complete_sign_census']['interval_horner_part_count'],516)
        self.assertEqual(interval['complete_sign_census']['interval_horner_failure_count'],0)
        self.assertTrue(interval['boundary_certificates']['lower_root_unique_and_simple'])
        self.assertTrue(interval['boundary_certificates']['upper_root_unique_and_simple'])
        atlas=d['obstruction_atlas']
        self.assertEqual(atlas['source_obstruction_count'],83)
        self.assertEqual(atlas['endpoint_released_strict_pass_count'],76)
        self.assertEqual(atlas['residual_obstruction_count'],7)
        self.assertEqual(atlas['residual_failure_names'],{'reduced_cost_q_0':7})
        self.assertEqual(d['q0_replacement_stress']['strict_pass_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a97_endpoint_released_catalogue_and_phase_provenance(self):
        d=json.loads((ROOT/'results'/'a97_endpoint_released_obstruction_catalogue.json').read_text())
        self.assertEqual(len(d['records']),83)
        self.assertEqual(sum(item['endpoint_released_result']['status']=='pass' for item in d['records']),76)
        residual=[item for item in d['records'] if item['endpoint_released_result']['status']!='pass']
        self.assertEqual([(item['maximum'],item['witness'],item['compressed_maximizer_contact']) for item in residual],[
            (396,'13/100',70),(443,'13/100',78),(449,'13/100',79),(455,'13/100',80),
            (484,'13/100',85),(490,'13/100',86),(496,'13/100',87),
        ])
        self.assertTrue(all(item['endpoint_released_result']['failure']['name']=='reduced_cost_q_0' for item in residual))
        self.assertEqual(len(d['residual_q0_replacement_tests']),7)
        interval_phase=json.loads((ROOT/'provenance'/'a97_phase'/'a97_interval_phase.json').read_text())
        atlas_phase=json.loads((ROOT/'provenance'/'a97_phase'/'a97_atlas_phase.json').read_text())
        self.assertTrue(interval_phase['pass'])
        self.assertEqual(len(atlas_phase['records']),83)



    def test_a98_unrestricted_full_lp_resolution(self):
        d=json.loads((ROOT/'results'/'a98_full_lp_active_set_resolution_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M396')
        self.assertEqual(d['resolved_active_set']['P_support'],[70,396])
        self.assertEqual(d['resolved_active_set']['Q_support'],[0,1,198,199])
        self.assertEqual(d['resolved_active_set']['active_bands'],[['alpha',1],['beta',-1]])
        self.assertEqual(d['strict_KKT_certificate']['strict_condition_count'],801)
        self.assertEqual(d['strict_KKT_certificate']['unrestricted_atom_reduced_cost_count'],788)
        self.assertTrue(d['strict_KKT_certificate']['unique_global_optimum'])
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a98_exact_certificate(self):
        d=json.loads((ROOT/'results'/'a98_full_lp_active_set_certificate.json').read_text())
        self.assertEqual(d['active_set']['P_support'],[70,396])
        self.assertEqual(d['active_set']['Q_support'],[0,1,198,199])
        self.assertEqual(len(d['basic_variables']),7)
        self.assertEqual(len(d['active_dual_multipliers']),2)
        self.assertEqual(len(d['reduced_costs']),788)
        self.assertEqual(len(d['inactive_band_slacks']),4)
        self.assertTrue(all(item['sign']==1 for item in d['basic_variables']))
        self.assertTrue(all(item['sign']==1 for item in d['active_dual_multipliers']))
        self.assertTrue(all(item['sign']==1 for item in d['reduced_costs']))
        self.assertTrue(all(item['sign']==1 for item in d['inactive_band_slacks']))
        self.assertTrue(d['objective']['equal'])

    def test_a99_q0q1_interval_and_residual_atlas(self):
        d=json.loads((ROOT/'results'/'a99_q0q1_interval_and_residual_atlas_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_Q0Q1_M396_INTERVAL_AND_TWO_OF_SIX_REMAINING_RESIDUAL_RESOLUTIONS')
        self.assertEqual(d['M396_interval_theorem']['condition_count'],801)
        self.assertEqual(d['M396_interval_theorem']['nonboundary_sign_failure_count'],0)
        self.assertTrue(d['M396_interval_theorem']['pass'])
        self.assertEqual(d['remaining_residual_atlas']['strict_pass_count'],2)
        self.assertEqual(d['remaining_residual_atlas']['failure_count'],4)
        self.assertEqual(d['remaining_residual_atlas']['pass_keys'],[[455,'13/100',80],[496,'13/100',87]])
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a99_interval_certificate_and_atlas(self):
        c=json.loads((ROOT/'results'/'a99_M396_q0q1_interval_certificate.json').read_text())
        self.assertTrue(c['pass'])
        self.assertEqual(c['strict_component']['lower_boundary_condition'],'inactive_slack_gamma_-1')
        self.assertEqual(c['strict_component']['upper_boundary_condition'],'basic_q_0')
        self.assertEqual(c['complete_sign_census']['nonboundary_numerator_count'],799)
        self.assertEqual(c['complete_sign_census']['nonboundary_sign_failure_count'],0)
        a=json.loads((ROOT/'results'/'a99_q0q1_remaining_residual_atlas.json').read_text())
        self.assertEqual(a['record_count'],6)
        self.assertEqual(a['strict_pass_count'],2)
        self.assertEqual(a['failure_count'],4)

    def test_a100_unrestricted_full_lp_resolution(self):
        d=json.loads((ROOT/'results'/'a100_full_lp_active_set_resolution_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_UNRESTRICTED_FULL_LP_ACTIVE_SET_RESOLUTION_AT_M443')
        self.assertEqual(d['resolved_active_set']['P_support'],[77,78,443])
        self.assertEqual(d['resolved_active_set']['Q_support'],[0,1,221,222])
        self.assertEqual(d['resolved_active_set']['active_bands'],[['alpha',1],['beta',-1],['gamma',-1]])
        self.assertEqual(d['strict_KKT_certificate']['strict_condition_count'],895)
        self.assertEqual(d['strict_KKT_certificate']['unrestricted_atom_reduced_cost_count'],881)
        self.assertTrue(d['strict_KKT_certificate']['unique_global_optimum'])
        self.assertTrue(all(v is True for v in d['gates'].values()))
        c=json.loads((ROOT/'results'/'a100_full_lp_active_set_certificate.json').read_text())
        self.assertEqual(len(c['basic_variables']),8)
        self.assertEqual(len(c['active_dual_multipliers']),3)
        self.assertEqual(len(c['reduced_costs']),881)
        self.assertEqual(len(c['inactive_band_slacks']),3)
        self.assertTrue(all(item['sign']==1 for item in c['basic_variables']))
        self.assertTrue(all(item['sign']==1 for item in c['active_dual_multipliers']))
        self.assertTrue(all(item['sign']==1 for item in c['reduced_costs']))
        self.assertTrue(all(item['sign']==1 for item in c['inactive_band_slacks']))
        self.assertTrue(c['objective']['equal'])
        p=json.loads((ROOT/'provenance'/'a100_high_precision_active_set_discovery.json').read_text())
        self.assertEqual(p['discovered_active_set']['P_support'],[77,78,443])
        self.assertEqual(p['discovered_active_set']['Q_support'],[0,1,221,222])
        self.assertEqual(p['discovered_active_set']['active_bands'],['alpha_plus','beta_minus','gamma_minus'])


    def test_a101_gamma_active_interval_and_residual_closure(self):
        d=json.loads((ROOT/'results'/'a101_gamma_active_interval_and_residual_closure_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_GAMMA_ACTIVE_M443_INTERVAL_AND_THREE_OF_THREE_FINAL_RESIDUAL_RESOLUTIONS')
        self.assertEqual(d['M443_interval_theorem']['condition_count'],895)
        self.assertEqual(d['M443_interval_theorem']['lower_boundary_condition'],'active_dual_gamma_-1')
        self.assertEqual(d['M443_interval_theorem']['upper_boundary_condition'],'basic_p_77')
        self.assertEqual(d['M443_interval_theorem']['nonboundary_numerator_count'],893)
        self.assertEqual(d['M443_interval_theorem']['nonboundary_sign_failure_count'],0)
        self.assertEqual(d['final_residual_atlas']['strict_pass_count'],3)
        self.assertEqual(d['final_residual_atlas']['failure_count'],0)
        self.assertEqual(d['final_residual_atlas']['total_strict_condition_count'],2873)
        self.assertEqual(d['A95_obstruction_closure_accounting']['resolved_count'],83)
        self.assertEqual(d['A95_obstruction_closure_accounting']['unresolved_rational_witness_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a101_interval_certificate_and_final_atlas(self):
        c=json.loads((ROOT/'results'/'a101_M443_gamma_active_interval_certificate.json').read_text())
        self.assertTrue(c['pass'])
        self.assertEqual(c['symbolic_reduction']['common_denominator_term_count'],7)
        self.assertTrue(c['symbolic_reduction']['common_denominator_strictly_positive_on_boundary_hull'])
        self.assertTrue(c['boundary_certificates']['lower_root_unique_and_simple'])
        self.assertTrue(c['boundary_certificates']['upper_root_unique_and_simple'])
        self.assertEqual(c['complete_sign_census']['nonboundary_numerator_count'],893)
        self.assertEqual(c['complete_sign_census']['nonboundary_sign_failure_count'],0)
        a=json.loads((ROOT/'results'/'a101_gamma_active_final_residual_atlas.json').read_text())
        self.assertEqual(a['record_count'],3)
        self.assertEqual(a['strict_pass_count'],3)
        self.assertEqual(a['failure_count'],0)
        self.assertEqual(a['pass_keys'],[[449,'13/100',79],[484,'13/100',85],[490,'13/100',86]])
        self.assertEqual([item['gamma_active_result']['condition_count'] for item in a['records']],[907,977,989])
        self.assertTrue(all(item['gamma_active_result']['strict_global_KKT_pass'] for item in a['records']))
        self.assertTrue(all(record['sign']==1 for item in a['records'] for record in item['gamma_active_result']['condition_records']))

    def test_a102_complete_rational_witness_lift_atlas(self):
        d=json.loads((ROOT/'results'/'a102_complete_rational_witness_lift_atlas_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_COMPLETE_EXACT_1063_RATIONAL_WITNESS_LIFT_ATLAS')
        self.assertEqual(d['gate_count'],23)
        self.assertEqual(d['pass_count'],23)
        atlas=d['complete_atlas']
        self.assertEqual(atlas['witness_count'],1063)
        self.assertEqual(atlas['unique_key_count'],1063)
        self.assertEqual(atlas['broad_resolution_class_counts'],{
            'legacy_natural':980,
            'endpoint_released_gamma_inactive':76,
            'q0q1_gamma_inactive':3,
            'q0q1_gamma_active':4,
        })
        self.assertEqual(atlas['detailed_resolution_class_counts'],{
            'legacy_three_band_gamma_plus':922,
            'legacy_three_band_gamma_minus':18,
            'legacy_two_band_compressed':40,
            'endpoint_released_gamma_inactive':76,
            'q0q1_gamma_inactive':3,
            'q0q1_gamma_active':4,
        })
        self.assertEqual(atlas['total_exact_KKT_condition_count'],676847)
        self.assertEqual(atlas['independent_exact_replay_count'],183)
        self.assertEqual(atlas['natural_stratified_replay_count'],100)
        self.assertEqual(atlas['post_A95_obstruction_replay_count'],83)
        self.assertEqual(atlas['source_certificate_validation_failure_count'],0)
        self.assertEqual(atlas['exact_replay_failure_count'],0)
        self.assertEqual(atlas['source_replay_mismatch_count'],0)
        self.assertEqual(d['obstruction_closure']['unresolved_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a102_complete_catalogue_and_provenance(self):
        d=json.loads((ROOT/'results'/'a102_complete_rational_witness_lift_atlas_catalogue.json').read_text())
        self.assertEqual(d['summary']['record_count'],1063)
        self.assertEqual(d['summary']['unique_key_count'],1063)
        self.assertEqual(d['summary']['duplicate_key_count'],0)
        self.assertEqual(d['summary']['routing_failure_count'],0)
        self.assertEqual(d['summary']['independent_exact_replay_count'],183)
        self.assertEqual(len(d['records']),1063)
        self.assertEqual(len({item['key'] for item in d['records']}),1063)
        self.assertTrue(all(item['source_certificate_validation']['strict_global_KKT_pass'] for item in d['records']))
        replayed=[item for item in d['records'] if item['exact_replay'].get('performed_in_A102')]
        self.assertEqual(len(replayed),183)
        self.assertTrue(all(item['exact_replay']['strict_global_KKT_pass'] for item in replayed))
        self.assertEqual(d['failures']['duplicate_keys'],[])
        self.assertEqual(d['failures']['routing_failures'],[])
        self.assertEqual(d['failures']['exact_replay_failures'],[])
        self.assertEqual(d['failures']['source_replay_mismatches'],[])
        h=json.loads((ROOT/'provenance'/'a102_complete_atlas'/'a102_source_certificate_hashes.json').read_text())
        self.assertEqual(h['source_count'],18)
        self.assertEqual(len(h['sources']),18)


    def test_a103_endpoint_released_continuum_segment_atlas(self):
        d=json.loads((ROOT/'results'/'a103_endpoint_released_continuum_segment_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_76_ENDPOINT_RELEASED_SEGMENTS_WITH_25_FULL_AND_51_PARTIAL_COMPONENTS')
        self.assertEqual(d['gate_count'],23)
        self.assertEqual(d['pass_count'],23)
        a=d['continuum_atlas']
        self.assertEqual(a['record_count'],76)
        self.assertEqual(a['unique_key_count'],76)
        self.assertEqual(a['status_counts'],{'proper_strict_subcomponent':51,'full_segment_coverage':25})
        self.assertEqual(a['condition_count'],54944)
        self.assertEqual(a['numerator_plus_denominator_count'],55020)
        self.assertEqual(a['selected_boundary_count'],55)
        self.assertEqual(a['outside_counterexample_count'],55)
        self.assertEqual(a['core_failure_count'],0)
        self.assertEqual(a['root_failure_count'],0)
        self.assertEqual(a['hull_failure_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a103_catalogue_boundary_certificates(self):
        d=json.loads((ROOT/'results'/'a103_endpoint_released_continuum_segment_catalogue.json').read_text())
        self.assertEqual(d['summary']['record_count'],76)
        self.assertEqual(len(d['records']),76)
        self.assertEqual(len({item['key'] for item in d['records']}),76)
        self.assertEqual(sum(item['condition_count'] for item in d['records']),54944)
        self.assertEqual(sum(item['numerator_plus_denominator_count'] for item in d['records']),55020)
        self.assertTrue(all(item['certificate_summary']['failure_count']==0 for item in d['records']))
        self.assertTrue(all(item['certificate_summary']['root_failure_count']==0 for item in d['records']))
        selected=[]
        for item in d['records']:
            for side in ('selected_left_boundary','selected_right_boundary'):
                b=item['strict_component'][side]
                if b is not None:
                    selected.append(b)
                    self.assertTrue(b['unique_simple_in_bracket'])
        self.assertEqual(len(selected),55)
        self.assertEqual(sum(len(item['outside_counterexamples']) for item in d['records']),55)
        self.assertEqual(d['failures']['duplicate_keys'],[])
        self.assertEqual(d['failures']['missing_keys'],[])
        self.assertEqual(d['failures']['extra_keys'],[])
        self.assertEqual(d['failures']['nonnegative_outside_counterexamples'],[])


    def test_a103_sample_exact_replay_validation(self):
        v=json.loads((ROOT/'provenance'/'a103_continuum_atlas'/'a103_sample_replay_validation.json').read_text())
        self.assertEqual(v['verdict'],'PASS_SAMPLE_EXACT_CHUNK_REPLAY_MATCH')
        self.assertEqual(v['replay_source_slice'],[0,4])
        self.assertEqual(v['record_count'],4)
        self.assertTrue(v['normalized_records_match_committed_chunk'])


    def test_a104_exceptional_q0q1_continuum_segment_atlas(self):
        d=json.loads((ROOT/'results'/'a104_exceptional_q0q1_continuum_segment_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_SEVEN_EXCEPTIONAL_Q0Q1_SEGMENTS_AS_TWO_SIDED_STRICT_SUBCOMPONENTS')
        self.assertEqual(d['gate_count'],22)
        self.assertEqual(d['pass_count'],22)
        a=d['continuum_atlas']
        self.assertEqual(a['record_count'],7)
        self.assertEqual(a['unique_key_count'],7)
        self.assertEqual(a['status_counts'],{'proper_two_sided_strict_subcomponent':7})
        self.assertEqual(a['architecture_counts'],{'q0q1_gamma_inactive':3,'q0q1_gamma_active':4})
        self.assertEqual(a['condition_count'],6489)
        self.assertEqual(a['numerator_plus_denominator_count'],6496)
        self.assertEqual(a['candidate_root_count'],25)
        self.assertEqual(a['selected_boundary_count'],14)
        self.assertEqual(a['root_ordering_check_count'],11)
        self.assertEqual(a['outside_counterexample_count'],14)
        self.assertEqual(a['core_failure_count'],0)
        self.assertEqual(a['root_failure_count'],0)
        self.assertEqual(a['ordering_failure_count'],0)
        self.assertEqual(a['hull_failure_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a104_catalogue_exact_boundaries_and_counterexamples(self):
        d=json.loads((ROOT/'results'/'a104_exceptional_q0q1_continuum_segment_catalogue.json').read_text())
        self.assertEqual(len(d['records']),7)
        self.assertEqual([item['maximum'] for item in d['records']],[396,443,449,455,484,490,496])
        self.assertTrue(all(item['status']=='proper_two_sided_strict_subcomponent' for item in d['records']))
        self.assertTrue(all(item['condition_count_matches_A102_source'] for item in d['records']))
        self.assertTrue(all(item['core_certificate']['failure_count']==0 for item in d['records']))
        self.assertTrue(all(item['nonselected_boundary_hull_certificate']['failure_count']==0 for item in d['records']))
        selected=[]
        for item in d['records']:
            self.assertEqual(len(item['outside_counterexamples']),2)
            self.assertTrue(all(counterexample['sign']==-1 for counterexample in item['outside_counterexamples']))
            self.assertEqual(item['root_ordering_certificate']['failure_count'],0)
            for side in ('selected_left_boundary','selected_right_boundary'):
                boundary=item['strict_component'][side]
                selected.append(boundary)
                self.assertTrue(boundary['unique_simple_in_bracket'])
        self.assertEqual(len(selected),14)
        self.assertEqual(d['failures']['condition_count_mismatches'],[])
        self.assertEqual(d['failures']['nonnegative_outside_counterexamples'],[])

    def test_a104_seven_record_provenance(self):
        paths=sorted((ROOT/'provenance'/'a104_exceptional_continuum_atlas').glob('a104_record_*.json'))
        self.assertEqual(len(paths),7)
        records=[json.loads(path.read_text()) for path in paths]
        self.assertEqual([item['maximum'] for item in records],[396,443,449,455,484,490,496])
        self.assertTrue(all(item['status']=='proper_two_sided_strict_subcomponent' for item in records))


    def test_a105_legacy_two_band_continuum_segment_atlas(self):
        d=json.loads((ROOT/'results'/'a105_legacy_two_band_continuum_segment_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_40_LEGACY_TWO_BAND_SEGMENTS_WITH_0_FULL_AND_40_PARTIAL_COMPONENTS')
        self.assertEqual(d['gate_count'],17)
        self.assertEqual(d['pass_count'],17)
        a=d['continuum_atlas']
        self.assertEqual(a['record_count'],40)
        self.assertEqual(a['unique_key_count'],40)
        self.assertEqual(a['status_counts'],{'proper_strict_subcomponent':40})
        self.assertEqual(a['phase_status_counts'],{
            'b_plus_1_to_b_plus_2::proper_strict_subcomponent':26,
            'unique_b_plus_2::proper_strict_subcomponent':14,
        })
        self.assertEqual(a['condition_count'],24312)
        self.assertEqual(a['numerator_plus_denominator_count'],24352)
        self.assertEqual(a['selected_boundary_count'],80)
        self.assertEqual(a['left_boundary_mechanisms'],{
            'inactive_slack_gamma_-1':6,
            'basic_p_support_mass':34,
        })
        self.assertEqual(a['right_boundary_mechanisms'],{'inactive_slack_gamma_+1':40})
        self.assertEqual(a['outside_counterexample_count'],80)
        self.assertEqual(a['core_failure_count'],0)
        self.assertEqual(a['hull_failure_count'],0)
        self.assertEqual(a['root_failure_count'],0)
        self.assertEqual(a['ordering_failure_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a105_catalogue_exact_boundaries_and_counterexamples(self):
        d=json.loads((ROOT/'results'/'a105_legacy_two_band_continuum_segment_catalogue.json').read_text())
        self.assertEqual(len(d['records']),40)
        self.assertEqual(len({item['key'] for item in d['records']}),40)
        self.assertTrue(all(item['status']=='proper_strict_subcomponent' for item in d['records']))
        self.assertTrue(all(item['condition_count_matches_A102_source'] for item in d['records']))
        self.assertEqual(sum(item['condition_count'] for item in d['records']),24312)
        self.assertEqual(sum(item['numerator_plus_denominator_count'] for item in d['records']),24352)
        self.assertEqual(sum(item['candidate_roots']['count'] for item in d['records']),181)
        self.assertEqual(sum(item['root_ordering_certificate']['check_count'] for item in d['records']),101)
        self.assertTrue(all(item['root_ordering_certificate']['failure_count']==0 for item in d['records']))
        self.assertTrue(all(item['core_certificate']['failure_count']==0 for item in d['records']))
        self.assertTrue(all(item['nonselected_boundary_hull_certificate']['failure_count']==0 for item in d['records']))
        selected=[]
        for item in d['records']:
            self.assertEqual(len(item['outside_counterexamples']),2)
            self.assertTrue(all(counterexample['sign']==-1 for counterexample in item['outside_counterexamples']))
            for side in ('selected_left_boundary','selected_right_boundary'):
                boundary=item['strict_component'][side]
                selected.append(boundary)
                self.assertTrue(boundary['unique_simple_in_bracket'])
        self.assertEqual(len(selected),80)
        self.assertEqual(d['failures']['duplicate_keys'],[])
        self.assertEqual(d['failures']['missing_keys'],[])
        self.assertEqual(d['failures']['extra_keys'],[])
        self.assertEqual(d['failures']['condition_count_mismatches'],[])
        self.assertEqual(d['failures']['nonnegative_outside_counterexamples'],[])

    def test_a105_forty_record_provenance(self):
        paths=sorted((ROOT/'provenance'/'a105_legacy_two_band_continuum_atlas'/'records').glob('a105_record_*.json'))
        self.assertEqual(len(paths),40)
        records=[json.loads(path.read_text()) for path in paths]
        self.assertEqual([item['maximum'] for item in records],[
            40,41,57,74,97,120,154,155,178,184,189,218,225,253,254,259,
            282,288,301,323,329,330,336,352,358,361,377,383,399,402,412,
            418,428,461,465,469,498,500,502,504,
        ])
        self.assertTrue(all(item['status']=='proper_strict_subcomponent' for item in records))
        self.assertTrue(all(len(item['outside_counterexamples'])==2 for item in records))
        replay=json.loads((ROOT/'provenance'/'a105_legacy_two_band_continuum_atlas'/'a105_standalone_replay_validation.json').read_text())
        self.assertEqual(replay['verdict'],'PASS_FULL_40_RECORD_EXACT_STANDALONE_REPLAY_MATCH')
        self.assertEqual(replay['record_count'],40)
        self.assertEqual(replay['comparison_count'],43)
        self.assertTrue(replay['all_equal'])
        self.assertTrue(all(item['equal'] for item in replay['comparisons']))

    def test_a106_legacy_gamma_minus_continuum_segment_atlas(self):
        d=json.loads((ROOT/'results'/'a106_legacy_gamma_minus_continuum_segment_results.json').read_text())
        self.assertEqual(d['verdict'],'PASS_EXACT_CONTINUUM_CLASSIFICATION_OF_18_LEGACY_GAMMA_MINUS_SEGMENTS_WITH_1_FULL_AND_17_PARTIAL_COMPONENTS')
        self.assertEqual(d['gate_count'],19)
        self.assertEqual(d['pass_count'],19)
        a=d['continuum_atlas']
        self.assertEqual(a['record_count'],18)
        self.assertEqual(a['unique_key_count'],18)
        self.assertEqual(a['status_counts'],{'proper_strict_subcomponent':17,'full_segment_coverage':1})
        self.assertEqual(a['phase_status_counts'],{
            'b_plus_1_to_b_plus_2::proper_strict_subcomponent':2,
            'b_plus_2_to_b_plus_1::full_segment_coverage':1,
            'unique_b_plus_1::proper_strict_subcomponent':1,
            'unique_b_plus_2::proper_strict_subcomponent':14,
        })
        self.assertEqual(a['condition_count'],2410)
        self.assertEqual(a['direct_rank_one_regression_comparison_count'],2410)
        self.assertEqual(a['direct_rank_one_regression_failure_count'],0)
        self.assertEqual(a['numerator_plus_denominator_count'],2428)
        self.assertEqual(a['selected_boundary_count'],17)
        self.assertEqual(a['left_boundary_mechanisms'],{'None':18})
        self.assertEqual(a['right_boundary_mechanisms'],{'basic_p_support_mass':17,'None':1})
        self.assertEqual(a['outside_counterexample_count'],17)
        self.assertEqual(a['core_failure_count'],0)
        self.assertEqual(a['hull_failure_count'],0)
        self.assertEqual(a['root_failure_count'],0)
        self.assertEqual(a['ordering_failure_count'],0)
        self.assertTrue(all(v is True for v in d['gates'].values()))

    def test_a106_catalogue_exact_boundaries_and_counterexamples(self):
        d=json.loads((ROOT/'results'/'a106_legacy_gamma_minus_continuum_segment_catalogue.json').read_text())
        records=d['records']
        self.assertEqual(len(records),18)
        self.assertEqual(len({item['key'] for item in records}),18)
        self.assertEqual([item['maximum'] for item in records],[18,23,28,29,34,35,45,51,56,62,68,79,85,91,96,102,108,114])
        self.assertTrue(all(item['condition_count_matches_A102_source'] for item in records))
        self.assertEqual(sum(item['condition_count'] for item in records),2410)
        self.assertEqual(sum(item['numerator_plus_denominator_count'] for item in records),2428)
        self.assertEqual(sum(item['candidate_roots']['count'] for item in records),22)
        self.assertEqual(sum(item['root_ordering_certificate']['check_count'] for item in records),5)
        self.assertTrue(all(item['root_ordering_certificate']['failure_count']==0 for item in records))
        self.assertTrue(all(item['core_certificate']['failure_count']==0 for item in records))
        self.assertTrue(all(item['nonselected_boundary_hull_certificate']['failure_count']==0 for item in records))
        full=[item for item in records if item['status']=='full_segment_coverage']
        self.assertEqual([item['maximum'] for item in full],[28])
        partial=[item for item in records if item['status']=='proper_strict_subcomponent']
        self.assertEqual(len(partial),17)
        selected=[]
        for item in partial:
            self.assertIsNone(item['strict_component']['selected_left_boundary'])
            boundary=item['strict_component']['selected_right_boundary']
            self.assertIsNotNone(boundary)
            self.assertTrue(boundary['condition'].startswith('basic_p_'))
            self.assertTrue(boundary['unique_simple_in_bracket'])
            self.assertEqual(len(item['outside_counterexamples']),1)
            self.assertEqual(item['outside_counterexamples'][0]['sign'],-1)
            selected.append(boundary)
        self.assertEqual(len(selected),17)
        self.assertEqual(d['failures']['duplicate_keys'],[])
        self.assertEqual(d['failures']['missing_keys'],[])
        self.assertEqual(d['failures']['extra_keys'],[])
        self.assertEqual(d['failures']['condition_count_mismatches'],[])
        self.assertEqual(d['failures']['nonnegative_outside_counterexamples'],[])

    def test_a106_eighteen_record_provenance_and_standalone_replay(self):
        base=ROOT/'provenance'/'a106_legacy_gamma_minus_continuum_atlas'
        paths=sorted((base/'records').glob('a106_record_*.json'))
        self.assertEqual(len(paths),18)
        records=[json.loads(path.read_text()) for path in paths]
        self.assertEqual([item['maximum'] for item in records],[18,23,28,29,34,35,45,51,56,62,68,79,85,91,96,102,108,114])
        replay=json.loads((base/'a106_standalone_replay_validation.json').read_text())
        self.assertEqual(replay['verdict'],'PASS_FULL_18_RECORD_EXACT_STANDALONE_REPLAY_MATCH')
        self.assertEqual(replay['record_count'],18)
        self.assertEqual(replay['comparison_count'],21)
        self.assertTrue(replay['all_equal'])
        self.assertTrue(all(item['equal'] for item in replay['comparisons']))

if __name__=='__main__': unittest.main()

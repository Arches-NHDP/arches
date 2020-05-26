<?php

$session = "https://heidicon.ub.uni-heidelberg.de/api/session";
$infos = file_get_contents( $session );
$json = json_decode( strip_tags( $infos ), true );
$token = $json[ 'token' ];
$html = "";
$html_en = "";
/*print_r($token);*/
$url = "https://heidicon.ub.uni-heidelberg.de/api/session/authenticate?token=$token&method=easydb&login=$login&password=$password";

// Authenticate the Session

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_CUSTOMREQUEST, "POST" );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
curl_setopt( $ch, CURLOPT_HTTPHEADER, array(
	'Content-Type: application/vnd.api+json;charset=UTF-8' ) );

curl_exec( $ch );

// Request Data from EasyDB

$data_string = file_get_contents( 'https://projects.zo.uni-heidelberg.de/cats/heidicon/data/objects.json' );
$search_url = "https://heidicon.ub.uni-heidelberg.de/api/v1/search?token=$token";
$ch = curl_init( $search_url );

curl_setopt( $ch, CURLOPT_CUSTOMREQUEST, "POST" );
curl_setopt( $ch, CURLOPT_POSTFIELDS, $data_string );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
curl_setopt( $ch, CURLOPT_HTTPHEADER, array(
	'Content-Type: application/vnd.api+json;charset=UTF-8' ) );

$result_json = curl_exec( $ch );
$result_array = json_decode( strip_tags( $result_json ), true );

foreach ( $result_array[ 'objects' ] as $objects ) {
	$objekte[] = $objects[ 'objekte' ];
}


// Sort Array by file name

foreach ( $objekte as $key => $items ) {
	$sort[ $key ] = $items[ '_reverse_nested:ressourcen:lk_objekt_id' ][ 0 ][ 'res_kommentar_intern' ];
}
array_multisort( $sort, SORT_ASC, $objekte );


// Group Array by internal comment field

$grouped = array();

foreach ( $objekte as $key => $item ) {
	$grouped[ $item[ 'obj_kommentar_intern' ] ][ $key ] = $item;
}

arsort( $grouped );

// Key as Gallery title

foreach ( $grouped as $key => $subarrays ) {

	$key = substr( $key, strpos( $key, "#" ) + 1 );
	$html .= '<h3>' . $key . '</h3>';
	$html .= '<div class="gallery_container">';
	foreach ( $subarrays as $images ) {
		$html .= '<a data-fancybox="' . $images[ 'obj_kommentar_intern' ] . '" title="' . $images[ 'obj_titel' ][ 'de-DE' ] . '" data-caption="<b>' . $images[ 'obj_titel' ][ 'de-DE' ] . '</b>&nbsp;[ID:' . $images[ '_reverse_nested:ressourcen:lk_objekt_id' ][ 0 ][ '_system_object_id' ] . ']<br><i>© ' . $images[ 'obj_creditline' ] . '</i>" href="' . $images[ '_reverse_nested:ressourcen:lk_objekt_id' ][ 0 ][ 'asset' ][ 0 ][ 'versions' ][ 'huge' ][ 'download_url' ] . '"><img src="' . $images[ '_reverse_nested:ressourcen:lk_objekt_id' ][ 0 ][ 'asset' ][ 0 ][ 'versions' ][ 'huge' ][ 'download_url' ] . '"></a>';
	}
	$html .= '</div>';

// English Array

	$html_en .= '<h3>' . $key . '</h3>';
	$html_en .= '<div class="gallery_container">';
	foreach ( $subarrays as $images ) {

		if ( isset( $images[ 'obj_titel' ][ 'en-US' ] ) ) {
			$title_en = $images[ 'obj_titel' ][ 'en-US' ];
		} else {
			$title_en = $images[ 'obj_titel' ][ 'de-DE' ];
		}

		$html_en .= '<a data-fancybox="' . $images[ 'obj_kommentar_intern' ] . '" title="' . $title_en . '" data-caption="<b>' . $title_en . '</b>&nbsp;[ID:' . $images[ '_reverse_nested:ressourcen:lk_objekt_id' ][ 0 ][ '_system_object_id' ] . ']<br><i>© ' . $images[ 'obj_creditline' ] . '</i>" href="' . $images[ '_reverse_nested:ressourcen:lk_objekt_id' ][ 0 ][ 'asset' ][ 0 ][ 'versions' ][ 'huge' ][ 'download_url' ] . '"><img src="' . $images[ '_reverse_nested:ressourcen:lk_objekt_id' ][ 0 ][ 'asset' ][ 0 ][ 'versions' ][ 'huge' ][ 'download_url' ] . '"></a>';
	}
	$html_en .= '</div>';
}







?>
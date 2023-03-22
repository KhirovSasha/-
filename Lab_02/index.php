<?php

require_once 'vendor/autoload.php'; 

$phpWord = \PhpOffice\PhpWord\IOFactory::load('example.docx');

$elements = $phpWord->getSections()[0]->getElements();

foreach ($elements as $element) {
    if ($element instanceof \PhpOffice\PhpWord\Element\TextRun) {
        foreach ($element->getElements() as $text) {
            if ($text instanceof \PhpOffice\PhpWord\Element\Text) {
                echo $text->getText() . " ";
            }
        }
        echo PHP_EOL;
    }
}